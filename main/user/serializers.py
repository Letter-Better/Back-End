from rest_framework import serializers
from .models import (
    User,
    Status,
    Friend
)

class UserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_lenght=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        write_only_fields = ('password',)

    def validate_email(self, value):
        return value.lower()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_lenght=200)

    def validate_email(self, value):
        return value.lower()
