from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('user/login/', views.obtain_auth_token, name='auth_token'),
    path('user/', include('user.urls', namespace='user'))
]
