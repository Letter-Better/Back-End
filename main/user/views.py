from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    EmailSerializer,
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
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            generated_code = uuid.uuid4().hex[:6]

            # TODO: Email Service: send code

            print("-"*10 + generated_code + "-"*10)
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
            else: return Response({"detail": "code must match."}, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
