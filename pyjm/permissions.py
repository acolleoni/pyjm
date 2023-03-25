from rest_framework import permissions


class AuthCheck(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.user.is_staff:
            return True
        return False