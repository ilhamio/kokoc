from rest_framework.routers import DefaultRouter
from charity.views import CharityViewSet, CharitySubscriptionViewSet, TransactionViewSet
from django.urls import path, include

router = DefaultRouter()
subscription_router = DefaultRouter()

router.register(r'charity', CharityViewSet)
subscription_router.register(r'charity-subscription', CharitySubscriptionViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(subscription_router.urls)),

]