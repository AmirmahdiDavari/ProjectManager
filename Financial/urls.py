from django.urls import path
from .views import ViewFinancial

urlpatterns = [
    path('', ViewFinancial.as_view()),

]
