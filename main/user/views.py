from os import stat
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    EmailSerializer,
    CodeSerializer,
)
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
from .models import User
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from main.settings import REDIS
import uuid


class UserRegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            generated_code = uuid.uuid4().hex[:6]

            # TODO: Email Service: send code

            print("-" * 10 + generated_code + "-" * 10)
            REDIS.set(generated_code, serializer.validated_data["email"])
            return Response({"detail": "success"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class EmailValidateView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            code, email = serializer.validated_data["code"], serializer.validated_data["email"]
            redis_code = REDIS.get(code)
            if redis_code.decode() == email:
                user = serializer.save()
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=HTTP_200_OK)
            else:
                return Response({"detail": "code must match."}, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "user not found."}, status=HTTP_400_BAD_REQUEST)
            generated_code = uuid.uuid4().hex[:16]
            print("-" * 20 + generated_code + "-" * 20)
            # TODO: Email Service: send code

            REDIS.set(generated_code, email)
            return Response({"detail": "email sended."}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ValidateForgotPassword(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, format=None):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            code, new_pass = serializer.validated_data["code"], serializer.validated_data["password"]
            value = REDIS.get(code)
            if value != None:
                try:
                    user = User.objects.get(email=value.decode())
                except User.DoesNotExist:
                    return Response({"detail": "not found"}, status=HTTP_400_BAD_REQUEST)
                user.set_password(new_pass)
                return Response({"detail": "pass changed"}, status=HTTP_202_ACCEPTED)
            return Response({"detail": "code not valid"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
