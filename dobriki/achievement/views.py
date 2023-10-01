from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from achievement.models import Achievement, UserAchievement
from achievement.serializers import AchievementSerializer, UserAchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class UserAchievementViewSet(viewsets.ModelViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer
