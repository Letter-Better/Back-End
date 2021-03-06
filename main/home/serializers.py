from rest_framework import serializers
from online.models import OnlineRanking
from campaign.models import CampaignRanking
from user.models import (
    User, Status, Friend
)


# TODO: add User relation in (OnlineRankingSerializer,CampaignRankingSerializer,StatusSerializer)
class OnlineRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineRanking
        fields = ("rank", "user")


class CampaignRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignRanking
        fields = ("rank", "user")


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("rank", "user")


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ("friends",)
