from django.urls import path
from .views import RoomView, CreateRoomView

app_name = 'online'

urlpatterns = [
    #path('', )
    path('create/', CreateRoomView.as_view(), name='create'),
    path('<str:room_code>/', RoomView.as_view(), name='room'),
]
