from django.urls import path
from .views import (
    UserRegisterView,
    GetTokenView,
    EmailValidateView,
    ForgotPasswordView,
    ValidateForgotPassword,
)

app_name = "user"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register-validate/', EmailValidateView.as_view(), name='register_validate'),
    path('login/', GetTokenView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot-password-validate/', ValidateForgotPassword.as_view(), name='forgot_password_validate')
]
