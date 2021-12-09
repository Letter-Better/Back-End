from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('user/', include('user.urls', namespace='user')),
]
