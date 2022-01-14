from os import name
from django.urls import path
from .consumers import NotificationConsumer

websocket_urlpatterns = [
    path("ws/notif/", NotificationConsumer.as_asgi(), name="notification"),
]
