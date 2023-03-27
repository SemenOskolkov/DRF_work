from rest_framework.permissions import BasePermission


class ModeratorPerms(BasePermission):  # permission на модератора

    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE']:
            return False
        return request.user.has_perms(['study.view_lesson', 'study.change_lesson', 'study.change_course', 'study.view_course'])


class SuperUserPerms(BasePermission):  # permission на суперпользователя

    def has_permission(self, request, view):
        return request.user.is_superuser


class OwnerPerms(BasePermission):  # permission на владельца

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.owner:
            return True
        return False
