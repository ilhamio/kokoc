from rest_framework import permissions


class ArticlePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'destroy', 'partial_update', 'update']:
            return request.user.is_authenticated and request.user.is_admin
        elif view.action in ['like', 'unlike', 'fans']:
            return request.user.is_authenticated
        else:
            return False


class ArticleCategoryPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'destroy', 'partial_update', 'update']:
            return request.user.is_authenticated and request.user.is_admin
        else:
            return False
