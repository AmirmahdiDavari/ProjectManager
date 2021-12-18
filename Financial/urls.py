from django.urls import path
from .views import Viewfinancial

urlpatterns = [
    path('', Viewfinancial.as_view()),

]
