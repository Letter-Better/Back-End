from rest_framework import serializers
from online.models import OnlineRanking
from campaign.models import CampaignRanking
from user.models import (
    User, Status, Friend
)


class OnlineRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnlineRanking
        fields = ("rank", "user", "win", "lose")

class CampaignRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampaignRanking
        fields = ("rank", "user", "win", "lose")

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'
