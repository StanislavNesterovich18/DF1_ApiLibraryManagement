from rest_framework import routers

from books.views import BookViewSet, AuthorViewSet

app_name = 'books'

router = routers.DefaultRouter()
router.register(r"books", BookViewSet, basename="book")
router.register(r"authors", AuthorViewSet, basename="author")

urlpatterns = router.urls
print(urlpatterns)
