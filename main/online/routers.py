from django.urls import path
from .consumers import OnlineGameConsumer

wensocketurlpatterns = [
    path('ws/room/<str:room_code>/', OnlineGameConsumer.as_asgi(), name="room_socket"),
]