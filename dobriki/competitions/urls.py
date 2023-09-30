from rest_framework.routers import DefaultRouter

from competitions.views import UserTeamViewSet

router = DefaultRouter()
router.register(r'teams', UserTeamViewSet)

urlpatterns = router.urls
