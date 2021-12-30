from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateRoomSerializer
from .models import RoomMember, Room
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

class CreateRoomView(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated]
    throttle_classes = []

    def post(self, request, format=None):
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(commit=False)
            RoomMember.objects.create(room=room, members=room.creator).save()
            data = {"redirect_url": reverse('online:room', request=request)}
            return Response(data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RoomView(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated]
    throttle_classes = []

    def get(self, room_code):
        try:
            room_ins = Room.objects.get(room_code=room_code)
        except Room.DoesNotExist:
            return Response({"redirect": reverse('home:404', request=self.request)})
        
        #if room_ins.
    
    def post(self, room_code): ...