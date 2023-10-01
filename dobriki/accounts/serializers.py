from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from activity.models import Aim
from competitions.models import UserTeam
from competitions.serializers import UserTeamSerializer

UserModel = get_user_model()


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = '__all__'


class AimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aim
        exclude = ('user',)


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aim
        exclude = ('user',)


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    teams = serializers.SerializerMethodField(read_only=True)
    aim = serializers.SerializerMethodField(read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    height = serializers.IntegerField(source='userprofile.height', required=False)
    weight = serializers.DecimalField(source='userprofile.weight', max_digits=5, decimal_places=2, required=False)
    age = serializers.IntegerField(source='userprofile.age', required=False)

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        model = UserModel
        fields = ['id', *extra_fields, 'teams', 'aim', 'subscription', 'height', 'weight', 'age']
        read_only_fields = ('email', 'date_joined')

    def get_teams(self, obj):
        return UserTeamSerializer(obj.teams, many=True).data

    def get_aim(self, obj):
        return AimSerializer(obj.aim, many=True).data

    def get_subscription(self, obj):
        return AimSerializer(obj.subscription, many=True).data
