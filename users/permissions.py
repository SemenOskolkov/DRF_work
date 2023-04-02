from rest_framework.permissions import BasePermission


class OwnProfileEditPermission(BasePermission):  # Задача со звездочкой из эталона

    def has_permission(self, request, view):
        return request.user == view.get_object()