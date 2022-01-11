from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import StatusSerializer
from user.models import Status

class HomePage(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        model_data = Status.objects.all()
        seria = StatusSerializer(model_data, many=True)
        return Response(seria.data)


class DashBoard(APIView):
    """
    
    """
    permission_classes = [IsAuthenticated]

    def get(self, request): ...
