from re import I
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, RoomMember

class OnlineGameConsumer(AsyncJsonWebsocketConsumer):
    async def websocet_connect(self, event):
        self.room_code = self.scope["url_router"]["kwargs"]["room_code"]
        self.user = self.scope["user"]

        await self.channel_layer.group_add(
            self.room_code,
            self.channel_name
        )
        
        try:
            room = database_sync_to_async(Room.objects.get(room_code=self.room_code))
        except Room.DoesNotExist:
            ...

        
        if database_sync_to_async(RoomMember.objects.filter(room_id=room.id, members=self.user.id).exists()):
            ...
