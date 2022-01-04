from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, RoomMember

class OnlineGameConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        self.room_code = self.scope["url_route"]["kwargs"]["room_code"]
        self.user = self.scope["user"]
        print(self.user)
        await self.channel_layer.group_add(
            self.room_code,
            self.channel_name
        )
        
        try:
            room = database_sync_to_async(Room.objects.get(room_code=self.room_code))
        except Room.DoesNotExist:
            print("error room_code")

        
        if database_sync_to_async(RoomMember.objects.filter(room_id=room.id, members=1).exists()):
            print("yay")
        await self.accept()

        

        
    async def websocket_disconnect(self, event):
        ...

    async def websocket_receive(self, message):
        ...
         

"""

"""