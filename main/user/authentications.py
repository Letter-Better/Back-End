from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.backends import BaseBackend
from rest_framework.exceptions import AuthenticationFailed
from .models import User

class UsernameBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and user.is_active == True:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmailBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password) and user.is_active == True:
                return user
        except User.DoesNotExist:
            raise AuthenticationFailed

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
