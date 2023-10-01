from django.urls import path
from rest_framework.routers import DefaultRouter
from activity.views import ActivityViewSet

router = DefaultRouter()
router.register(r'', ActivityViewSet)


urlpatterns = router.urls
