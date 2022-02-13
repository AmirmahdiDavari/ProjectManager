from django.urls import path, include
from django.contrib import admin
from .views import *


app_name = "AddUser"

urlpatterns = [
    path('profile', profile, name="get user profile"),
    path('loginPhone', loginPhone, name='login with phone'),
    path('loginEmail', loginEmail, name='login with email')
]
