from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model


class ExpertSerializer (serializers.ModelSerializer):
    enddate=serializers.HiddenField
    class Meta:
        model = get_user_model()
        fields="__all__"

class UpdateStatusTasktSerializer (serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["Estimated_end", 'status']
