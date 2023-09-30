from django.contrib.auth import get_user_model
from rest_framework import serializers

from competitions.models import UserTeam, PersonalCompetition

User = get_user_model()


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username']


class UserTeamSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, required=False)

    class Meta:
        model = UserTeam
        fields = '__all__'


class PersonalCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCompetition
        fields = '__all__'
