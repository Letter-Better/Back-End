from rest_framework.permissions import BasePermission

class IsMember(BasePermission):
    message = ""

    def has_permission(self, request, view):
        VALID_METHOD = ("GET", "POST", "UPDATE")
        return request.user == 1 and request.method in VALID_METHOD

class IsAdmin(BasePermission):
    message = 'You are not an admin.'

    def has_permission(self, request, view) -> bool:
        INVALID_METHOD = ("DELETE",)
        return request.user.role == 2 and not request.method in INVALID_METHOD

class IsOwner(BasePermission):
    message = 'You are not an owner.'

    def has_permission(self, request, view) -> bool:
        return request.user.role == 3
