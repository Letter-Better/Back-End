from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Room, RoomMember


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
        extra_kwargs = {
            'creator': {'required': False},
            'time_of_draw': {'required': True},
            'round': {'required': True},
            'number_of_users': {'required': True},
            'room_type': {'required': True},
            'difficulty': {'required': True},
            }

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'creator',
            'time_of_draw',
            'round',
            'number_of_users',
            'room_type',
            'difficulty',
        )

class RoomMemberSerializer(serializers.ModelSerializer):
    room_data = RoomSerializer(many=True)

    class Meta:
        model = RoomMember
        fields = (
            'room',
            'members',
            'room_data'
        )




