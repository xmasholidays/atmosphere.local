from rest_framework import permissions


class IsLocalhostRequest(permissions.BasePermission):

    def has_permission(self, request, view):
        return self._get_client_ip(request) == '127.0.0.1'

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
