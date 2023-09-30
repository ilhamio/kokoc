from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    # filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    serializer_class = ActivitySerializer
    ordering_fields = ['name', 'coefficient']
    ordering = ['name']
    search_fields = ['name', 'description']
