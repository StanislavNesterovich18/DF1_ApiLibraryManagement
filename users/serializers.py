from rest_framework.serializers import ModelSerializer

from users.models import User


class UserCreateSerializer(ModelSerializer):
    """ Сериализатор для создания нового пользователя.
    Используется при регистрации. Принимает только email и пароль,
    что минимизирует количество обязательных полей для ввода."""
    class Meta:
        model = User
        fields = ("email", "password")


class UserSerializer(ModelSerializer):
    """Сериализатор для чтения и обновления данных пользователя.
    Используется для отображения профиля пользователя и его редактирования.
    В отличие от UserCreateSerializer, включает все публичные поля модели."""
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

