from rest_framework.serializers import ModelSerializer

from books.models import Author, Book


class BookSerializer(ModelSerializer):
    """ Сериализатор для модели Book. Преобразует данные модели Book в формат JSON и обратно.
    Включает все поля модели для сериализации."""
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    """    Сериализатор для модели Author. Преобразует данные модели Author в формат JSON и обратно.
    Включает все поля модели для сериализации."""
    class Meta:
        model = Author
        fields = '__all__'
