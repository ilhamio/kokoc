from rest_framework.routers import DefaultRouter
from activity.views import ActivityViewSet

router = DefaultRouter()
router.register(r'activity', ActivityViewSet)

urlpatterns = router.urls
