from rest_framework import permissions


class IsLocalhostRequest(permissions.BasePermission):

    def has_permission(self, request, view):
        return True
