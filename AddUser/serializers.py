from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        # fields = ['id','full_name','image']
        fields = ['id','image','first_name', 'last_name']
        # exclude=('type','money')
        # depth=1


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','username']
        # exclude=('type','money')
        # depth=1
