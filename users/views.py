from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import UserCreateSerializer, UserSerializer


class CreateApiView(generics.CreateAPIView):
    """ Регистрация нового пользователя.
    Эндпоинт для создания аккаунта. Доступен без авторизации (AllowAny).
    Принимает email и пароль, автоматически хеширует пароль перед сохранением.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Получение данных профиля пользователя.
    Доступен только авторизованным пользователям (IsAuthenticated).
    Возвращает полную информацию о пользователе по его ID.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление данных профиля пользователя.
    Доступен только авторизованным пользователям.
    Поддерживает как полное обновление (PUT), так и частичное (PATCH).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление (деактивация) пользователя.
    Доступен только авторизованным пользователям.
    Полностью удаляет пользователя из базы данных."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
