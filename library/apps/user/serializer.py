from .models import Users
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Users(**validated_data)
        user.set_password(password)
        user.save()
        return {
        "username": user.username,
        "email": user.email,
        }
    
