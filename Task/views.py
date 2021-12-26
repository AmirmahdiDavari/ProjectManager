from rest_framework.response import Response
from datetime import datetime
from jalali_date import datetime2jalali
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .serializers import UpdateStatusTasktSerializer, allTasktSerializer, AllTaskSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class updateTask (RetrieveUpdateAPIView):
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



class DashbordType(ListAPIView):
    serializer_class = allTasktSerializer
    permission_classes = (IsAuthenticated,)

    @property
    def get_queryset(self):
        Type = self.request.GET.get('type')
        Type = int(Type)
        datetime_object = datetime.now()
        if Type == 1:
            queryset = Task.objects.filter(Expert=self.request.user, Estimated_end__isnull=True)

            return queryset
        elif Type == 2:
            queryset = Task.objects.filter(Expert=self.request.user, Estimated_end__lte=datetime_object)
            if queryset:
                queryset = Task.objects.filter(Expert=self.request.user, )
                return queryset
            else:
                return Response({"mesage": "TASKI VOVJOD NADARAD"})
        elif Type == 3:
            queryset = Task.objects.filter(Expert=self.request.user, status=1)
            return queryset
        else:
            return Response({'mesege': "TYPE RA BE DOROSTI VARED KONID"})


def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
