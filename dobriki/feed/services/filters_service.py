from feed.models import ArticleTag, ArticleCategory
from feed.serializers import ArticleCategoryPreviewSerializer, ArticleTagSerializer


def get_all_filters():
    return {'tags': ArticleTagSerializer(ArticleTag.objects.all(), many=True).data,
            'categories': ArticleCategoryPreviewSerializer(ArticleCategory.objects.all(), many=True).data}
