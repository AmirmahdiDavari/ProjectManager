from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username','email']
        # exclude=('type','money')
        # depth=1


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username']
        # exclude=('type','money')
        # depth=1
