from django.contrib import admin

from feed.models import *


class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(ArticleAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )


class ArticleCategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'description')


class ArticleTagAdmin(admin.ModelAdmin):
    fields = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(Like)
