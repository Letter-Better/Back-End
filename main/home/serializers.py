from rest_framework import serializers
from online.models import OnlineRanking
from campaign.models import CampaignRanking
from user.models import (
    User, Status, Friend
)


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

class HomePage(serializers.Serializer):
    online_ranking = CampaignRankingSerializer(many=True, read_only=True)
    campaign_ranking = StatusSerializer(many=True, read_only=True)
    users_ranking = FriendSerializer(many=True, read_only=True)


