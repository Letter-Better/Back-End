from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('user/', include('user.urls', namespace='user')),
    path('room/', include('online.urls', namespace='online')),
]
