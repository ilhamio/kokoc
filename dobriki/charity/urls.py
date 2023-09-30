from rest_framework.routers import DefaultRouter
from charity.views import CharityViewSet, CharitySubscriptionViewSet

router = DefaultRouter()
router.register(r'charity', CharityViewSet)
router.register(r'charity-subscription', CharitySubscriptionViewSet)

urlpatterns = router.urls
