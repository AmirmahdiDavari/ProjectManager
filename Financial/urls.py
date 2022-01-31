from django.urls import path
from .views import *

urlpatterns = [
    path('', FinancialList.as_view()),

]
