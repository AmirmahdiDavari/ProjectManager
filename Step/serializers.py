from rest_framework import serializers
from .models import Step
from AddUser.serializers import *
from jalali_date import datetime2jalali, date2jalali
from jalali_date.fields import JalaliDateField


class StepSerializer(serializers.ModelSerializer):
    # experts=UserSerializer(many=True)
    # scrumMaster=UserSerializer(many=True)
    class Meta:
        model = Step
        fields = "__all__"
