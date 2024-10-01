from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id_user',
            'role',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'is_active',
        ]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        pass


class UserUpsertSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        pass
