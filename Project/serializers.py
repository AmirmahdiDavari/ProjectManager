from jalali_date import datetime2jalali, date2jalali
from jalali_date.fields import JalaliDateField
from rest_framework import serializers
from AddUser.serializers import *
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    experts = UserSerializer(many=True)
    scrumMaster = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title"]
