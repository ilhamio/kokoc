from rest_framework.routers import DefaultRouter
from .views import ConfigViewSet

router = DefaultRouter()
router.register(r'configs', ConfigViewSet)

urlpatterns = router.urls
