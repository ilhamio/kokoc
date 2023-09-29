from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from pytils.translit import slugify
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Like(models.Model):
    """ Like on article """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Лайк от {self.user}"

    class Meta:
        verbose_name = "Лайк статьи"
        verbose_name_plural = "Лайки статей"


class Article(models.Model):
    """Article model"""
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, verbose_name="Автор статьи", blank=True)
    title = models.CharField(max_length=256, verbose_name="Заголовок статьи")
    content = models.TextField(verbose_name="Содержание")
    tags = models.ManyToManyField('ArticleTag', verbose_name="Теги")
    category = models.ForeignKey('ArticleCategory', on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    created_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    last_updated_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата последнего обновления")
    likes = GenericRelation('Like', verbose_name='Лайки')
    image = models.ImageField(upload_to='blog/articles', max_length=100, blank=True, null=True, verbose_name="Обложка")
    preview_text = models.TextField(max_length=150, verbose_name="Текст превью (будет отображаться в списке статей)")

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleCategory(models.Model):
    """ Article category for filtering articles """
    title = models.CharField(max_length=128, verbose_name="Название категории")
    slug = models.SlugField(max_length=128, verbose_name="Уникальный код категории", unique=True)
    created_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ArticleCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class ArticleTag(models.Model):
    """ Article mini tags for searching """
    slug = models.SlugField(max_length=128, verbose_name="Уникальный код (Заполняется автоматически)", unique=True)
    name = models.CharField(max_length=128, verbose_name="Название тега", unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ArticleTag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги статей"
