from rest_framework.decorators import action
from rest_framework.response import Response

from feed.serializers import ArticleAuthorSerializer
from feed.services import likes_service


class LikedMixin:
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        likes_service.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`."""
        obj = self.get_object()
        likes_service.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = likes_service.get_fans(obj)
        serializer = ArticleAuthorSerializer(fans, many=True)
        return Response(serializer.data)
