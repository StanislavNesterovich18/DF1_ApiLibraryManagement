from rest_framework import permissions


class ModerationPermission(permissions.BasePermission):
    """Разрешение для модераторов.
      Даёт доступ только пользователям, состоящим в группе "Модератор".
      Используется для эндпоинтов, требующих прав модерации контента.
      """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Модератор").exists()


class IsOwner(permissions.BasePermission):
    """Разрешение для владельца объекта.
    Даёт доступ только тому пользователю, который является владельцем объекта.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
