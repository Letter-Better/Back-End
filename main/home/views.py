from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CampaignRankingSerializer, OnlineRankingSerializer, StatusSerializer
from user.models import Status
from online.models import OnlineRanking
from campaign.models import CampaignRanking


class CampRankView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        model_data = CampaignRanking.objects.all()[:20]
        seria = CampaignRankingSerializer(model_data, many=True)
        return Response(seria.data)


class OnlineRankView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        model_data = OnlineRanking.objects.all()[:20]
        seria = OnlineRankingSerializer(model_data, many=True)
        return Response(seria.data)


class StatusRankView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        model_data = Status.objects.all()[:20]
        seria = StatusSerializer(model_data, many=True)
        return Response(seria.data)
