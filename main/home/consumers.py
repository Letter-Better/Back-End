from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def websocket_connect(self, message):
        if isinstance(self.scope["user"], AnonymousUser):
            self.close()
        else: ...

    
    async def websocket_disconnect(self, close_code): ...

    async def websocket_receive(self, message): ...