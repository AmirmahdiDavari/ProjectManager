from django.urls import path
from .views import updateTask, Dashbord,TaskProgect

urlpatterns = [
    path('<int:pk>', updateTask.as_view()),
    path('task/1', Dashbord.as_view()),
    path('project /<int:pk>/tasks', TaskProgect.as_view()),

]
