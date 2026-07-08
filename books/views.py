from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.filters import BookFilter
from books.models import Book, Author
from books.serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    queryset = Book.objects.all()

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve", "update", "destroy", "partial_update"]:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
