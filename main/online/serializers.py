from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Room


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'craetor',
            'time_of_draw',
            'round',
            'number_of_users',
            'room_type',
            'difficulty'
        )
    
    def create(self, validated_data):
        self.user = CurrentUserDefault()
        return super().create(validated_data)

