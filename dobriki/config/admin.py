from django.contrib import admin
from .models import Config

class ConfigAdmin(admin.ModelAdmin):
    fields = ('name', 'coefficient', 'description')

admin.site.register(Config, ConfigAdmin)
