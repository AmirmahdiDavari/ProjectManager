from rest_framework import serializers
from .models import scheduling_Expert, scheduling_ScrumMaster, project_scheduling


class scheduling_Expert_Serializer(serializers.ModelSerializer):
    class Meta:
        model = scheduling_Expert
        fields = "__all__"


class scheduling_ScrumMaster_Serializer(serializers.ModelSerializer):
    class Meta:
        model = scheduling_ScrumMaster
        fields = "__all__"


class project_scheduling_Serializer(serializers.ModelSerializer):
    class Meta:
        model = project_scheduling
        fields = "__all__"
