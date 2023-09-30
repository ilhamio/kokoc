from django.contrib import admin
from charity.models import Charity, CharitySubscription


# class CharitySubscriptionAdmin(admin.ModelAdmin):
#     fields = ('user', 'charity', 'sum', 'days', 'created_at')

admin.site.register(Charity)
# admin.site.register(CharitySubscription, CharitySubscriptionAdmin)
admin.site.register(CharitySubscription)
