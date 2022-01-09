from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

class HomePage(APIView):
    """
    
    """
    permission_classes = [AllowAny]

    def get(self, request): ...


class DashBoard(APIView):
    """
    
    """
    permission_classes = [IsAuthenticated]

    def get(self, request): ...
