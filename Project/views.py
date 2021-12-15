from django.shortcuts import render,get_object_or_404
from .models import Project
from .serializers import updateProjecttSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import  RetrieveAPIView
from django.views.generic import DetailView


class ProjectDetile(RetrieveAPIView ):
    queryset = Project.objects.all()
    serializer_class=updateProjecttSerializer

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Project,pk=self.kwargs.get("pk"))


from jalali_date import datetime2jalali, date2jalali

from jalali_date import datetime2jalali, date2jalali

def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')