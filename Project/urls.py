from django.conf import settings
from django.templatetags.static import static
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'project'
urlpatterns = [
    # path('<int:pk>', ProjectDetile.as_view()),
    # path('', ProjectList.as_view()),
    path('',ProjectList.as_view()),
    path('members/<int:id>',ProjectMembers.as_view()),

    path('list_project',list_project.as_view(),name= 'list_project'),
]
