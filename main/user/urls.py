from django.urls import path
from .views import (
    UserRegisterView,
    GetTokenView,
)

app_name = "user"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', GetTokenView.as_view(), name='login')
]
