from rest_framework import serializers
from .models import (
    User,
    Status,
    Friend
)


class UserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'code')
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


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=200)

    def validate_email(self, value):
        return value.lower()


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=16)
    password = serializers.CharField()
