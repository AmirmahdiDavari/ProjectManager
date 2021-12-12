from rest_framework import serializers
from .models import financial

class ViewfinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = financial
        fields = "__all__"
        exclude=('type','money')

