from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *

app_name = 'project'
urlpatterns = [

    path('', adminpage  ),

]
