from django_filters import rest_framework as rfilter
from rest_framework import filters

from feed.models import Article


class ArticleFilter(rfilter.FilterSet):
    category = rfilter.CharFilter(field_name="category__slug", lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['category']

class TagsFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        tags = request.query_params.get('tags', None)
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__slug__in=tags).distinct()

        return queryset