from rest_framework import serializers
from finch.models import SandboxAccess


class SandboxAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SandboxAccess
        fields = '__all__'
