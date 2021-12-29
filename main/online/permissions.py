from rest_framework import permissions

class RoomExists(permissions.BasePermission):
    message = '...'

    def has_permission(self, request, view): ...