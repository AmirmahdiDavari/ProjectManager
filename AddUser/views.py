from django.shortcuts import render
from django.views.generic import UpdateView
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer
from .models import MyUser


class Profile(ListCreateAPIView):
    model=MyUser
    serializer_class = UserSerializer
    def get_object(self):
        queryset=MyUser.objects.get(pk=self.request.MyUser.pk)
        return queryset
