from django.db import models

from users.models import User


class Author(models.Model):
    """ Модель автора. Содержит информацию об авторе книги: ФИО автора, фото,
    а также даты создания и обновления записи."""
    fullname = models.CharField(max_length=200, verbose_name="Ф.И.О автора")
    avatar_image = models.ImageField(upload_to="author_images", null=True, blank=True, verbose_name="Фото")
    create_ad = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_ad = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    """Модель книги.Содержит полную информацию о книге: название, обложку, количество страниц, вес, год публикации,
     жанр,связь на модель автора с помощью Fk, страну, ISBN(уникальный номер книги), возрастное ограничение и обложку."""
    TYPE_CHOICES = [
        ('HARD', 'Твердый переплёт'),
        ('SOFT', 'Мягкий переплёт'),
    ]
    GENRE_CHOICES = [
        ('Horror', 'Ужасы'),
        ('Comedy', 'Коммедия'),
        ('Sci-Fi', 'Фантастика'),
        ('Animation', 'Мульфильмы'),
        ('Drama', 'Драма'),
    ]
    name_book = models.CharField(max_length=200, verbose_name="Название книги")
    type_skin = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
        default='HARD',
        verbose_name = "Тип обложки"
    )
    number_pages = models.PositiveIntegerField(verbose_name="Кол-во страниц")
    weight_book = models.PositiveIntegerField(verbose_name="Вес книги")
    year_publication = models.PositiveIntegerField(verbose_name="Год книги")
    genre = models.CharField(
        max_length=9,
        choices=GENRE_CHOICES,
        default='Sci-Fi',
        verbose_name="Жанр книги"
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    country = models.CharField(max_length=200, verbose_name="Страна")
    isbn = models.CharField(max_length=50,unique=True, verbose_name="Уникальный ISBN")
    age_limit = models.PositiveIntegerField(verbose_name="Возрастное ограничение")
    image = models.ImageField(upload_to="images", null=True, blank=True,verbose_name="Обложка")
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_book

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class IssuingBookUser(models.Model):
    """Модель выдачи книги пользователю. Отслеживает факт выдачи книги конкретному пользователю
    и текущий статус пользования книгой."""
    STATUS_CHOICES = [
        ('Received', 'Получил'),
        ('Returned', 'Вернул'),
        ('Lost', 'Утеряна'),
        ('Spoiled', 'Испорчена'),
    ]
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default='Received',
        verbose_name="Статус пользования"
    )

