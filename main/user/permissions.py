from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view) -> bool:
        INVALID_METHOD = ("DELETE",)
        message = 'You are not an admin.'
        return request.user.role == 2 and not request.method in INVALID_METHOD

class IsOwner(BasePermission):

    def has_permission(self, request, view) -> bool:
        message = 'You are not an owner.'
        return request.user.role == 3
