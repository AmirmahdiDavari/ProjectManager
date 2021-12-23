from django.urls import path
from .views import updateTask,TaskUpdate,TaskList,Dashbord1,Dashbord2,Dashbord3

urlpatterns = [
    path('<int:pk>/',updateTask.as_view()),
    path('tasts/',TaskList.as_view()),
    path('Task/1',Dashbord1.as_view()),
    path('Task/2',Dashbord2.as_view()),
    path('Task/3',Dashbord3.as_view()),

]