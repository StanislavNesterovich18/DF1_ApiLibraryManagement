import os
from http.client import responses
from itertools import count

import django
from django.urls import reverse
from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.conf import settings
from rest_framework.test import APITestCase

from books.models import Author
from users.models import User


class BooksTestCase(APITestCase):
    """    Набор тестов для API управления книгами. Тестирует все CRUD операции с книгами:"""
    id_book = 0

    def setUp(self):
        """Подготовка данных перед каждым тестом.
        Создает:
            - Тестового пользователя с email "test@test.com"
            - Аутентифицирует клиент
            - Создает тестового автора "А.С. Пушкин"
        Выполняется перед каждым тестом: готовим данные."""
        super().setUp()
        self.user = User.objects.create(
            email="test@test.com",
        )
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(
            fullname="А.С. Пушкин",
        )

    def test_book_create_wrong(self):
        """Тест создания книги с некорректными данными. Проверяет, что при отправке невалидных данных
        (несуществующие поля) API возвращает ошибку 400. Ожидаемый результат: HTTP 400 Bad Request"""
        url = reverse("books:book-list")
        response = self.client.post(url, data={'name': 'Test Lesson', 'url_video': 'Test book'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_create(self):
        """Тест успешного создания книги. Проверяет создание книги со всеми обязательными полями.
        Сохраняет ID созданной книги для использования в других тестах."""
        url = reverse("books:book-list")
        response = self.client.post(url, data={'name_book': "Test book",
                                               'number_pages': "123",
                                               'weight_book': "123",
                                               'year_publication': "1988",
                                               'country': "Россия",
                                               'isbn': "123123123123",
                                               'age_limit': "12",
                                               'author': self.author.id
                                               })
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['name_book'], 'Test book')
        self.id_book = data['id']

    def test_book_retrieve(self):
        """      Тест получения детальной информации о книге.
        Создает книгу через test_book_create и запрашивает ее данные.
        Ожидаемый результат: HTTP 200 OK"""
        self.test_book_create()
        url = reverse("books:book-detail", kwargs={'pk': self.id_book})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_update(self):
        """ Тест обновления данных книги. Создает книгу, затем обновляет ее название.
        Ожидаемый результат:
            - HTTP 200 OK
            - Название книги обновлено на "Test book NEW" """
        self.test_book_create()
        url = reverse("books:book-detail", kwargs={'pk': self.id_book})
        response = self.client.put(url, data={'name_book': "Test book NEW",
                                               'number_pages': "123",
                                               'weight_book': "123",
                                               'year_publication': "1988",
                                               'country': "Россия",
                                               'isbn': "123123123123",
                                               'age_limit': "12",
                                               'author': self.author.id
                                               })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name_book'], 'Test book NEW')


    def test_book_destroy(self):
        self.test_book_create()
        url = reverse("books:book-detail", kwargs={'pk': self.id_book})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_book_list(self):
        self.test_book_create()
        url = reverse("books:book-list")
        response = self.client.get(url)
        data = response.json()
        self.assertTrue(data[-1].get('name_book') == 'Test book')
        self.assertTrue(len(data[-1]) >= 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


