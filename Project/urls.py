from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *

app_name = 'project'
urlpatterns = [

    path('', ProjectList.as_view()),
    path('<int:id>/members', ProjectMembers.as_view()),
    path('list_project', list_project.as_view(), name='list_project'),
]
