from django.shortcuts import render
# from rest_framework.generics
from jalali_date import datetime2jalali

from .models import project_scheduling
def projectscheduling(request):
    scheduling=project_scheduling.objects.all()
    mydict={"time":scheduling}
    return render(request,"scheduling.html",context=mydict)



def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')