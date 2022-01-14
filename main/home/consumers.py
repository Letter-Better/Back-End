from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NotificationConsumer(AsyncJsonWebsocketConsumer):

    def websocket_connect(self):
        print(self.scope["user"])
    
    def websocket_disconnect(self, close_code): ...

    def websocket_receive(self, message): ...