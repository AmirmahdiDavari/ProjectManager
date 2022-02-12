from django.urls import path
from Task.views import TaskList,updateTask,TaskDetail,task_project,task_detile
from . import views
app_name = "Task"
urlpatterns = [

    path('list',TaskList.as_view()),
    path('list/<int:id>',TaskDetail.as_view()),
    path('task_project',task_project.as_view(),name='Task_project'),
    path('task_detile',task_detile.as_view(),name='task_detile'),
]
