from rest_framework.routers import DefaultRouter

from competitions.views import UserTeamViewSet, PersonalCompetitionViewSet

router = DefaultRouter()
router.register(r'teams', UserTeamViewSet)
router.register(r'personal', PersonalCompetitionViewSet)

urlpatterns = router.urls
