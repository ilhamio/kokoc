from django_filters import rest_framework as filters
from .models import CharitySubscription

class CharityFilterSet(filters.FilterSet):
    user_id = filters.NumberFilter(field_name="user__id")

    class Meta:
        model = CharitySubscription
        fields = ['user__id']