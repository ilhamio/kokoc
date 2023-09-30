from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from feed.models import Article, ArticleCategory, ArticleTag
from feed.services import likes_service
from markdown import markdown

User = get_user_model()


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleCategoryPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        exclude = ('description',)


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'


class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ArticlePreviewSerializer(serializers.ModelSerializer):
    category = ArticleCategoryPreviewSerializer(read_only=True)
    tags = ArticleTagSerializer(read_only=True, many=True)
    likes = SerializerMethodField('get_likes')
    author = ArticleAuthorSerializer()
    preview_text = serializers.CharField()

    class Meta:
        model = Article
        exclude = ('content',)

    def get_likes(self, obj):
        return obj.total_likes


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(read_only=True)
    tags = ArticleTagSerializer(read_only=True, many=True)
    likes = SerializerMethodField('get_likes')
    author = ArticleAuthorSerializer()
    content = SerializerMethodField('get_content')
    is_fan = SerializerMethodField('get_is_fan')

    class Meta:
        model = Article
        fields = '__all__'

    def get_likes(self, obj):
        return obj.total_likes

    def get_content(self, obj):
        content = markdown(obj.content)
        return content

    def get_is_fan(self, obj):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            return likes_service.is_fan(obj, user)
        return False
