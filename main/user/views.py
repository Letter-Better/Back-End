from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
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
            REDIS.set(request.data["email"], generated_code)
            return Response(status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class EmailValidateView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    
    def post(self, request, format=None):
        email = request.data["email"]
        try:
            user = User.objects.get(email=email)
            code = REDIS.get(email)
            if user.is_email_verified == False and code == request.data["code"]:
                user.is_email_verified = True
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                Response({"token": token.key})
        except User.DoesNotExist:
            return Response({"detail": "not found."})
