from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from competitions.models import UserTeam
from competitions.serializers import UserTeamSerializer


class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer

    @action(detail=True, methods=['POST'])
    def apply(self, request, pk=None):
        """Вступить в команду `obj`.
        """
        if not request.user.is_authenticated:
            return Response({'error': 'Not authenticated'}, status=401)
        obj: UserTeam = self.get_object()
        request.user.teams.add(obj)
        return Response({'result': "successfully applied"}, status=200)