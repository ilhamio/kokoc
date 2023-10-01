from django.contrib import admin
from .models import Activity, ActivityConverter

# class ActivityAdmin(admin.ModelAdmin):
#     fields = ('name', 'coefficient', 'description')

# admin.site.register(Activity, ActivityAdmin)
admin.site.register(Activity)
admin.site.register(ActivityConverter)