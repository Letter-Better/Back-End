from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateRoomSerializer
from .models import RoomMember
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
            return Response(room.room_code, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
