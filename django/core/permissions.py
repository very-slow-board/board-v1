from rest_framework import permissions


class IsGetOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user.is_authenticated
