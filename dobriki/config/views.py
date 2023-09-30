from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Config
from .serializers import ConfigSerializer

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    # filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    serializer_class = ConfigSerializer
    ordering_fields = ['name', 'coefficient']
    ordering = ['name']
    search_fields = ['name', 'description']
