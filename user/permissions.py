from rest_framework import permissions
from rest_framework.views import Request, View


class IsAccountOwner(permissions.BasePermission):
    ...
    # def has_object_permission(self, request, view: View, obj: User) -> bool:
    #     return request.user.is_authenticated and obj == request.user