import json
from django.utils import timezone
from datetime import date

from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from jalali_date import datetime2jalali, date2jalali
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import UpdateStatusTasktSerializer, allTasktSerializer, AllTaskSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class updateTask(RetrieveUpdateAPIView):
    serializer_class = UpdateStatusTasktSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset


class TaskList(ListAPIView, LoginRequiredMixin):
    permission_classes = (IsAuthenticated,)

    serializer_class = AllTaskSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(Expert=self.request.user)


class TaskUpdate(RetrieveUpdateAPIView, LoginRequiredMixin):
    serializer_class = UpdateStatusTasktSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(Expert=self.request.user, Estimated_end__isnull=True, status=1 | 2 | 3 | 0)


class Dashbord2(ListAPIView):
    serializer_class = allTasktSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Task.objects.filter(Expert=self.request.user, status=1)
        return queryset


class Dashbord3(ListAPIView):
    serializer_class = AllTaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        def diffNowDate(Estimated_end):
            from datetime import datetime
            fmt = '%Y-%m-%d'
            d2 = datetime.strptime(
                str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day), fmt)
            d1 = datetime.strptime(Estimated_end, fmt)
            e = (d2 - d1).days
            if e>=0:
                queryset = Task.objects.filter(Expert=self.request.user)
                return queryset
            else:
                return Response("aaaaaaaaaaaaaaaaaaaa")


class Dashbord1(ListAPIView):
    serializer_class = AllTaskSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):

        queryset = Task.objects.filter(Expert=self.request.user, Estimated_end__isnull=True)

        return HttpResponse(queryset)


def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

