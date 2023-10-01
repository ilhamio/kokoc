from django.contrib import admin
from charity.models import Charity, CharitySubscription


class CharitySubscriptionAdmin(admin.ModelAdmin):
    fields = ('user', 'charity', 'sum', 'days')

class CharityAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization_name', 'approved')
    list_filter = ('approved',)
    actions = ['approve_charities', 'reject_charities']

    def approve_charities(self, request, queryset):
        queryset.update(approved=True)

    def reject_charities(self, request, queryset):
        queryset.update(approved=False)


admin.site.register(Charity, CharityAdmin)
# admin.site.register(Charity)
admin.site.register(CharitySubscription)
