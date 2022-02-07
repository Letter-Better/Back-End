from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from channels.exceptions import StopConsumer
from .models import Room, RoomMember
from django.contrib.auth.models import AnonymousUser


class OnlineGameConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        self.room_code = self.scope["url_route"]["kwargs"]["room_code"]
        self.user = self.scope["user"]

        await self.channel_layer.group_add(
            self.room_code,
            self.channel_name
        )
        try:
            room = database_sync_to_async(Room.objects.get(room_code=self.room_code))
        except Room.DoesNotExist:
            self.close()
        if not isinstance(self.user, AnonymousUser):
            if database_sync_to_async(RoomMember.objects.filter(room_id=room.id, members=self.user).exists()):
                await self.accept()
            else:
                self.close()
        else:
            self.close()

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.room_code, self.channel_name
        )
        raise StopConsumer()

    async def websocket_receive(self, message):
        text_data = message.get('text', None)
        bytes_data = message.get('bytes', None)
