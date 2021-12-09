from django.urls import path
from .views import (
    UserRegisterView,
    GetTokenView,
    EmailValidateView
)

app_name = "user"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', GetTokenView.as_view(), name='login'),
    path('validate/', EmailValidateView.as_view(), name='validate')
]
