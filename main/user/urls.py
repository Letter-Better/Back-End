from django.urls import path
from .views import (
    UserRegisterView,
    #GetTokenView,
    EmailValidateView,
    ForgotPasswordView,
    ValidateForgotPassword,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "user"

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register-validate/', EmailValidateView.as_view(), name='register_validate'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot-password-validate/', ValidateForgotPassword.as_view(), name='forgot_password_validate')
]
