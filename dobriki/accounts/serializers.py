from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from activity.models import Aim
from charity.models import Transaction, CharitySubscription
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
        model = CharitySubscription
        exclude = ('user',)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ('user',)


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    teams = serializers.SerializerMethodField(read_only=True)
    aim = serializers.SerializerMethodField(read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)
    transactions = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            # We don't need to call the all-auth
            # username validator unless its installed
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
        fields = ['id', *extra_fields, 'teams', 'aim', 'subscription', 'transactions']
        read_only_fields = ('email', 'date_joined')

    def get_teams(self, obj):
        return UserTeamSerializer(obj.teams, many=True).data

    def get_aim(self, obj):
        aim = Aim.objects.get(user_id=obj.id)
        return AimSerializer(aim).data

    def get_subscription(self, obj):
        try:
            sub = CharitySubscription.objects.get(user_id=obj.id)
            return SubscriptionSerializer(sub).data
        except Exception:
            return None

    def get_transactions(self, obj):
        return TransactionSerializer(obj.transactions, many=True).data
