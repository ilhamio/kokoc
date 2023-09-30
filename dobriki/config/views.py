from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Config

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ['name', 'coefficient']
    ordering = ['name']
    search_fields = ['name', 'description']
