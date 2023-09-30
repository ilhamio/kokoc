from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from achievement.models import Achievement, UserAchievement
from achievement.serializers import AchievementSerializer, UserAchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class UserAchievementViewSet(viewsets.ModelViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer

    @action(detail=True, methods=['POST'])
    def apply(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=401)
        obj: UserAchievementSerializer = self.get_object()

        if obj.user != request.user:
            return Response({'error': 'You can only create subscriptions for yourself'}, status=403)
        ## additional verification
        request.user.charity_subscription.add(obj)
        return Response({'result': "successfully applied"}, status=200)
