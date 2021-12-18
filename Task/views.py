import json
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from jalali_date import datetime2jalali, date2jalali
from .models import Task
from .serializers import UpdateStatusTasktSerializer, DashbordTasktSerializer, AllTaskSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class updateTask(RetrieveUpdateAPIView):
    serializer_class = UpdateStatusTasktSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset


class Dashbord(ListAPIView):
    serializer_class = AllTaskSerializer

    def get_queryset(self):
        queryset = Task.objects.filter(Estimated_end__isnull=True)
        return queryset
    # elif int == 2:
    #     def get_queryset(self):
    #         queryset = Task.objects.filter(status=1)
    #
    #         return queryset


class TaskProgect(ListAPIView):
    queryset =Task.objects.filter(StepID__ProjectId=int)
    serializer_class = AllTaskSerializer

def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
