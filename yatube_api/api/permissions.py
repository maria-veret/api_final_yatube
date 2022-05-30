from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    message = 'Вы не являетесь автором'

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
