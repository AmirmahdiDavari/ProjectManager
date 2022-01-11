from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>', updateTask),
     path('withProjectId/<int:id>', getTaskWithProjectId),
]
