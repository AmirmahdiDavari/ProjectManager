from django.urls import path
from .views import updateTask, DashbordType, TaskList

urlpatterns = [
    path('<int:pk>/', updateTask.as_view()),
    path('tasts/', TaskList.as_view()),
    path('DashbordType/', DashbordType.as_view()),

]
