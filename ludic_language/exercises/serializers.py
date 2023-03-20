from rest_framework import serializers
from .models import RecorderMessage


class RecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecorderMessage
        fields = '__all__'