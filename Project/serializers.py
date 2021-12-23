from rest_framework import serializers
from .models import Project


class ListProjecttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
