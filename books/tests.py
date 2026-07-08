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
from users.models import User
from books.models import Author


class BooksTestCase(APITestCase):
    id_book = 0

    def setUp(self):
        """Выполняется перед каждым тестом: готовим данные."""
        super().setUp()
        self.user = User.objects.create(
            email="test@test.com",
        )
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(
            fullname="А.С. Пушкин",
        )

    def test_book_create_wrong(self):
        url = reverse("books:book-list")
        response = self.client.post(url, data={'name': 'Test Lesson', 'url_video': 'Test book'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_create(self):
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
        self.test_book_create()
        url = reverse("books:book-detail", kwargs={'pk': self.id_book})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_update(self):
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


