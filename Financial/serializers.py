from rest_framework import serializers
from .models import financial
from Project.serializers import *
from AddUser.serializers import *

class FinancialSerializer(serializers.ModelSerializer):
    project_id=ProjectTitleSerializer(many=False)
    userRecipientofmoney=UserNameSerializer(many=False)
    class Meta:
        model = financial
        fields = "__all__"
