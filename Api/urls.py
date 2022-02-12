from django.conf import settings
from django.templatetags.static import static
from django.urls import path
from .views import *
from . import views
# from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'Api'
urlpatterns = [
    # path('api_mg/',api_mg.as_view(),name= 'api_mg'),
    # path('api_mg/',views.api_mg,name= 'api_mg'),
    path('api_mg/',views.api_mg,name= 'api_mg'),
    path('task_mg/',views.task_mg,name='task_mg')
]
