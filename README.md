# Api Library Management

REST API для управления библиотекой с использованием Django Rest Framework (DRF).

---
В рамках выполнения поставленной задачи было разработано полнофункциональное REST API для управления библиотекой с использованием Django Rest Framework (DRF).
Реализован полный цикл управления книгами, авторами, пользователями и выдачей книг с соблюдением всех технических требований.

Реализованный функционал
1. Управление книгами (Books)
- Реализованы CRUD операции (создание, чтение, обновление, удаление) для книг

- Реализован поиск и фильтрация книг по:
- Названию (регистронезависимый поиск по части слова)
- Автору (по имени автора)
- Жанру
- Году издания (точное совпадение, больше/меньше)
- Реализована валидация данных при создании и обновлении книг

Управление авторами (Authors)
- Реализованы CRUD операции для авторов
- Реализован поиск авторов по имени (регистронезависимый)
- Обеспечена связь между книгами и авторами (внешние ключи)

Управление пользователями (Users)
- Реализована регистрация новых пользователей с валидацией данных
- Реализована JWT аутентификация с использованием djangorestframework-simplejwt:
- Получение access/refresh токенов
- Обновление токенов
- Проверка токенов
- Реализован профиль пользователя:
- Получение информации о текущем пользователе
- Обновление профиля

Выдача книг (Borrowings)
- Реализован учет выдачи/возврата книг пользователем
- Реализован учет утери книг
---

## Технологии
- **Backend**: Django 5.0+, Django Rest Framework 3.15+
- **База данных**: PostgreSQL 15
- **Аутентификация**: JWT (Simple JWT)
- **Документация**: drf-spectacular (OpenAPI 3.0)
- **Контейнеризация**: Docker, Docker Compose
- **Фильтрация**: django-filter
- **Тестирование**: pytest, coverage

---

## Функционал
- **Книги**: CRUD, поиск по названию/автору/жанру/году, фильтрация
- **Авторы**: CRUD, поиск по имени и году рождения
- **Пользователи**: Регистрация, JWT авторизация, профиль
- **Выдача книг**: Выдача, возврат, статус, история, проверка наличия

---

## Структура проекта

DF1_ApiLibraryManagement/

├── .venv/ # Виртуальное окружение
├── books/ # Управление книгами (модели, вьюхи, сериализаторы, фильтры)
├── users/ # Управление пользователями (регистрация, JWT)
├── config/ # Настройки Django (settings, urls, wsgi)
├── media/ # Загруженные файлы (обложки книг)
├── static/ # Статические файлы (CSS, JS)
├── htmlcov/ # Отчеты покрытия тестами
├── .env # Переменные окружения (не в Git)
├── .env_example # Пример переменных окружения
├── .gitignore # Игнорируемые файлы
├── docker-compose.yml # Docker Compose
├── Dockerfile # Docker образ
├── main.py # Точка входа для Docker
├── manage.py # Django management
├── poetry.lock # Фиксированные версии зависимостей
├── pyproject.toml # Зависимости Poetry
├── requirements.txt # Зависимости для pip
└── README.md # Документация


---

## 🚀 Установка и запуск через Docker

```bash
# 1. Клонировать репозиторий
git clone https://github.com/yourusername/library-api.git
cd library-api

# 2. Настроить переменные окружения
cp .env.example .env

# 3. Запустить контейнеры
docker-compose up -d --build

# 4. Применить миграции
docker-compose exec backend python manage.py migrate

# 5. Создать суперпользователя
docker-compose exec backend python manage.py createsuperuser

# 6. API доступно по адресам:
# API: http://localhost:8000/api/v1/
# Swagger: http://localhost:8000/api/docs/
# Admin: http://localhost:8000/admin/

```
## Аутентификация (JWT)

POST users/ registration/ 
POST users/ retrieve/<int:pk>/ 
POST users/ update/<int:pk>/ 
POST users/ destroy/<int:pk>/ 
POST users/ login/ 



## Книги (books)
GET    books/              - Список всех книг
POST   books/              - Создать книгу
GET    books/{id}/         - Получить книгу
PUT    books/{id}/         - Обновить книгу
PATCH  books/{id}/         - Частично обновить
DELETE books/{id}/         - Удалить книгу

## Пользователи (users)
GET    users/me/           - Информация о текущем пользователе
PUT    users/me/           - Обновить профиль

## Документация API 
Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

## Переменные окружения (.env)
DB_NAME=***
DB_USER=postgres
DB_PASSWORD=**
DB_HOST=127.0.0.1
DB_PORT=5432
SECRET_KEY=***
DEBUG=True
CELERY_RESULT_BACKEND
CELERY_BROKER_URL
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_USE_TLS
EMAIL_USE_SSL

## Основные зависимости (requirements.txt)

---

## Разработчик

Имя Фамилия - StanislavNesterovich18

Email: stas.nester18@mail.ru

---

## Лицензия
MIT License

---
Сделано с ❤️ с использованием Django Rest Framework 

