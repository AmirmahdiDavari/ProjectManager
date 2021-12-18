from django.shortcuts import render
from .models import financial
from .serializers import ViewfinancialSerializer
from rest_framework.generics import ListAPIView


class Viewfinancial(ListAPIView):
    queryset = financial.objects.all()
    serializer_class = ViewfinancialSerializer
