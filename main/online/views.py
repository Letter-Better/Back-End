from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from .serializers import (
    CreateRoomSerializer,
    RoomMemberSerializer,
    RoomSerializer,
)
from .models import RoomMember, Room
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

class CreateRoomView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = []

    def post(self, request):
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(creator=request.user)
            return Response(data={"redirect": room.room_code}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RoomView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = []

    def get(self, request, room_code):
        try:
            room_ins = Room.objects.get(room_code=room_code)
        except Room.DoesNotExist:
            return Response({"notfound": "nope"})#{"redirect": reverse('home:404', request=self.request)})

        if not RoomMember.objects.filter(room_id=room_ins.id, members_id=request.user.id).exists():
            return Response({"using post to join": "..."})
            
        # TODO: error from here
        my_data = RoomMemberSerializer(instance=room_ins)
        return Response(my_data.data)

    def post(self, request, room_code):
        try:
            room_ins = Room.objects.get(room_code=room_code)
        except Room.DoesNotExist:
            return Response({"notfound": "nope"})
        RoomMember.objects.craete(room=room_ins, members_id=request.user.id)
        my_data = RoomSerializer(room_ins)
        return Response(my_data.data)


