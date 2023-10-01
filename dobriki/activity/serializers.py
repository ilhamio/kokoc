from rest_framework import serializers
from .models import Activity, ActivitySnapshot


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ActivitySnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitySnapshot
        exclude = ('user',)
