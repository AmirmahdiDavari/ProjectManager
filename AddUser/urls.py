from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[
    path('profile',profile,name="get user profile"),
    path('loginPhone',loginPhone,name='login with phone'),
    path('loginEmail',loginEmail,name='login with email')
]