import django_filters

from books.models import Book, Author


class BookFilter(django_filters.rest_framework.FilterSet):
    author = django_filters.ModelChoiceFilter(
        field_name="author", queryset=Author.objects.all(), label="Автор"
    )
    type_skin = django_filters.ChoiceFilter(
        field_name="type_skin", choices=Book.TYPE_CHOICES, label="Тип обложки"
    )
    genre = django_filters.ChoiceFilter(
        field_name="genre", choices=Book.GENRE_CHOICES, label="Жанр книги"
    )

    class Meta:
        model = Book
        exclude = ['image']


class AuthorFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Author
        exclude = ['avatar_image']
