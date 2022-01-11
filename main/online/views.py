from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
)
from .serializers import (
    CreateRoomSerializer,
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
            RoomMember.objects.create(room=room)
            room.roommember.members.add(request.user.id)
            return Response(data={"redirect": room.room_code}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RoomView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = []

    def get(self, request, room_code):
        try:
            room = Room.objects.get(room_code=room_code)
        except Room.DoesNotExist:
            return Response({"not found": "noe"})

        if not RoomMember.objects.filter(room_id=room.id, members=request.user.id).exists():
            return Response({"using post to join": "..."})

        my_data = RoomSerializer(room)
        return Response(my_data.data)

    def post(self, request, room_code):
        try:
            room = Room.objects.get(room_code=room_code)
        except Room.DoesNotExist:
            return Response({"not found": "noe"})
        
        room.roommember.members.add(request.user.id)
        my_data = RoomSerializer(room)
        return Response(my_data.data)
