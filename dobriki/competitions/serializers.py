from django.contrib.auth import get_user_model
from rest_framework import serializers

from competitions.models import UserTeam

User = get_user_model()


class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = '__all__'
