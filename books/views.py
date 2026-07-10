from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.filters import BookFilter
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """   ViewSet для управления книгами. Предоставляет полный CRUD функционал для модели Book:
    list: получение списка всех книг, create: создание новой книги, retrieve: получение детальной информации о книге,
    update: полное обновление книги, partial_update: частичное обновление книги, destroy: удаление книг"""
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    queryset = Book.objects.all()

    def get_permissions(self):
        """Устанавливает права доступа для каждого действия. Возвращает: list: Список объектов разрешений
        для текущего действия"""
        if self.action in ["create", "list", "retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


class AuthorViewSet(viewsets.ModelViewSet):
    """ ViewSet для управления авторами. Предоставляет полный CRUD функционал для модели Author:
    list: получение списка всех книг, create: создание новой книги, retrieve: получение детальной информации о книге,
    update: полное обновление книги, partial_update: частичное обновление книги, destroy: удаление книг"""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_permissions(self):
        """Устанавливает права доступа для каждого действия. Возвращает: list: Список объектов разрешений
        для текущего действия"""
        if self.action in ["create", "list", "retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
