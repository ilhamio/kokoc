from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from competitions.models import UserTeam, PersonalCompetition
from competitions.serializers import UserTeamSerializer, PersonalCompetitionSerializer


class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer

    @swagger_auto_schema(method='post', request_body=no_body,
                         responses={200: "{'result': 'successfully applied'}", 401: "{'error': 'Not authenticated'}"})
    @action(detail=True, methods=['POST'])
    def apply(self, request, pk=None):
        """Вступить в команду `obj`.
        """
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=401)
        obj: UserTeam = self.get_object()
        request.user.teams.add(obj)
        return Response({'result': "successfully applied"}, status=200)


class PersonalCompetitionViewSet(viewsets.ModelViewSet):
    queryset = PersonalCompetition.objects.all()
    serializer_class = PersonalCompetitionSerializer


    @swagger_auto_schema(method='post', request_body=no_body,
                         responses={200: "{'result': 'successfully applied'}", 401: "{'error': 'Not authenticated'}"})
    @action(detail=True, methods=['POST'])
    def apply(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=401)
        obj: PersonalCompetition = self.get_object()
        request.user.personal_competitions.add(obj)
        return Response({'result': "successfully applied"}, status=200)

