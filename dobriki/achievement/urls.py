from rest_framework.routers import DefaultRouter
from achievement.views import AchievementViewSet, UserAchievementViewSet

router = DefaultRouter()
router.register(r'achievement', AchievementViewSet)
router.register(r'achievement-user', UserAchievementViewSet)

urlpatterns = router.urls
