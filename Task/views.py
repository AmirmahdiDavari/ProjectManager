import json
from rest_framework.generics import UpdateAPIView
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from rest_framework.response import Response
from .models import Task
from .serializers import UpdateStatusTasktSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class updateTask(RetrieveUpdateAPIView):
    serializer_class = UpdateStatusTasktSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset


class Dashbord(ListAPIView):
    serializer_class = UpdateStatusTasktSerializer

    def get_queryset(self):
        queryset = Task.objects.filter(Estimated_end__isnull=True)
        return queryset

    def get_queryset(self):
        queryset = Task.objects.filter(Estimated_end__isnull=True)
        response = {
            "mesage": 'mohtava baz ghardande shod'
        }
        return queryset

# class TaskList(ListAPIView):
#     # Define model
#     model = Task
#     # Define template
#     serializer_class = ViewTasktSerializer
#
#     def get_queryset(self):
#         # Set the default query set
#         # # Check the form value is submitted or not
#         # if self.request.GET.keys():
#         #     # Check the search keyword
#         #     if self.request.GET.get('src') != '':
#         #         keyword = self.request.GET.get('src')
#         #         # Set the query set based on search keyword
#         queryset = Task.objects.filter(endDate__isnull=True)
#         return queryset


# class UpdateTask (ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = UpdateTasktSerializer
