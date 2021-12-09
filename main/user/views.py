from django import conf
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    EmailValidateSerializer
)
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User
from main.settings import REDIS
import uuid

class GetTokenView(ObtainAuthToken):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            if user.is_email_verfied == True:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})

class UserRegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            generated_code = uuid.uuid4().hex[:6]
            print("-"*10 + generated_code + "-"*10)
            REDIS.set(serializer.validated_data["email"].lower(), generated_code)
            return Response({"detail": "success"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class EmailValidateView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    def post(self, request, format=None):
        # TODO: fix is_email_verfied name
        serializer = EmailValidateSerializer(data=request.data)
        if serializer.is_valid():
            email, code = serializer.validated_data["email"], serializer.validated_data["code"]
            try:
                user = User.defmanager.get(email=email.lower())
                redis_code = REDIS.get(email.lower())
                if user.is_email_verified == False and redis_code.decode() == code:
                    print("if True")
                    user.is_email_verified = True
                    user.save()
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({"token": token.key}, status=HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "not found."})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
