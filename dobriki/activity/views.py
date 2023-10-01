from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Activity, ActivitySnapshot
from .serializers import ActivitySerializer, ActivitySnapshotSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @swagger_auto_schema(method='post', request_body=ActivitySnapshotSerializer,
                         responses={201: ActivitySnapshotSerializer, 400: '{"error": "Wrong model!"}'})
    @action(detail=False, methods=['POST'])
    def snap(self, request):
        serializer = ActivitySnapshotSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"error": "Wrong model!"}, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        data['user'] = request.user
        activity_id = data['activity_type']
        del data['activity_type']
        ActivitySnapshot.objects.create(activity_type_id=activity_id, user_id=request.user.id, **data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)