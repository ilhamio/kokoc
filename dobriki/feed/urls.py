from rest_framework.routers import DefaultRouter
from feed.views import ArticleViewSet, ArticleCategoryViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'category', ArticleCategoryViewSet)

urlpatterns = router.urls
