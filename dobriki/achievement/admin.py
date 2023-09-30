from django.contrib import admin
from achievement.models import Achievement, UserAchievement


# class UserAchievementAdmin(admin.ModelAdmin):
#     fields = ('user', 'achievement', 'achieved_at')

admin.site.register(Achievement)
# admin.site.register(UserAchievement, UserAchievementAdmin)
admin.site.register(UserAchievement)
