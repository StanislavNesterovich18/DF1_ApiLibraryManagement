from rest_framework.serializers import ModelSerializer

from users.models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "avatar",
            "numbers_phone",
            "city",
            "is_active",
            "is_staff",
        )

