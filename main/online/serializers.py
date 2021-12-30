from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Room


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'creator',
            'time_of_draw',
            'round',
            'number_of_users',
            'room_type',
            'difficulty'
        )
        extra_kwargs = {'creator': {'required': False}}
    
    def create(self, validated_data):
        validated_data["creator"] = CurrentUserDefault()
        return super().create(validated_data)

