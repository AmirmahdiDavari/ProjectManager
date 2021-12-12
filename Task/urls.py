from django.urls import path
from .views import updateTask,Task

urlpatterns = [
    path('<int:pk>',updateTask.as_view()),
    # path('update/<int:pk>/',updateTask.as_view()),
    # path('Dashbord/',TaskList.as_view()),

]