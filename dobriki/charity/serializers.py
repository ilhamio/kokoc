from rest_framework import serializers
from charity.models import Charity, CharitySubscription


class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = '__all__'

class CharitySubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharitySubscription
        fields = '__all__'