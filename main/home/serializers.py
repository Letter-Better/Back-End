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
    online_ranking = OnlineRankingSerializer(many=True, read_only=True)
    campaign_ranking = CampaignRankingSerializer(many=True, read_only=True)

    class Meta:
        model = Status
        fields = ("rank", "user", "online_ranking", "campaign_ranking")

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ("friends",)



