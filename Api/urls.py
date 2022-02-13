from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.templatetags.static import static
from django.conf import settings
from django.urls import path
from .views import *
from . import views

app_name = 'Api'
urlpatterns = [

    path('api_mg/', views.api_mg, name='api_mg'),
    path('task_mg/', views.task_mg, name='task_mg')
]
