from django.urls import path
from .views import updateTask,DashbordType,TaskList,Dashbord3

urlpatterns = [
    path('<int:pk>/',updateTask.as_view()),
    path('tasts/',TaskList.as_view()),
    path('Task/3',Dashbord3.as_view()),
    path('DashbordType/',DashbordType.as_view()),

]