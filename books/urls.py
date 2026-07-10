"""URL-конфигурация для приложения books. Определяет маршруты REST API для работы с книгами и авторами."""
from rest_framework import routers

from books.views import AuthorViewSet, BookViewSet

app_name = 'books'

router = routers.DefaultRouter()
router.register(r"books", BookViewSet, basename="book")
router.register(r"authors", AuthorViewSet, basename="author")

urlpatterns = router.urls
