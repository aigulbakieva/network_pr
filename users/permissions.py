from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """Проверка активности пользователя."""

    def has_permission(self, request, view):
        return request.user.is_active
