from rest_framework import serializers
from charity.models import Charity, CharitySubscription


class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = '__all__'


class CharitySubscriptionSerializer(serializers.ModelSerializer):
    charity = CharitySerializer()
    class Meta:
        model = CharitySubscription
        exclude = ('user',)


class CreateCharitySubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharitySubscription
        fields = ['charity']
