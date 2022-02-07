from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Room, RoomMember
from user.models import User


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


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'full_name',
            'image',
            'friend_code'
        )


class RoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMember
        fields = (
            'members',
        )


class RoomSerializer(serializers.ModelSerializer):
    room_member = serializers.SerializerMethodField()

    def get_room_member(self, obj):
        return SimpleUserSerializer(obj.roommember.members, many=True).data

    class Meta:
        model = Room
        fields = (
            'creator',
            'time_of_draw',
            'round',
            'number_of_users',
            'room_type',
            'difficulty',
            'room_code',
            'room_member'
        )
