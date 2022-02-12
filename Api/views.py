from django.shortcuts import render , redirect
from django.views.generic.list import ListView
from Api.models import Message , Develop , Validation
from Task.models import  Task
from rest_framework.permissions import IsAuthenticated
from Project.models import Project

# Create your views here.
# class api_mg(ListView):
#     permission_classes=('IsAuthenticated',)
#     template_name="Api.html"
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return Message.objects.all() 
#         else:
#             return Message.objects.filter(task_id__expert=self.request.user)


def api_mg(request):
    permission_classes=('IsAuthenticated',)
    requestobj=request.GET.get('TaskId')
    message = Message.objects.filter(task_id__id=requestobj)
    validation = Validation.objects.filter(task_id__id=requestobj)
    develop = Develop.objects.filter(task_id__id=requestobj)
    project=Project.objects.all()
    return render(request , 'Api.html',context={'mes':message,'val':validation,'dev':develop,'pro':project})









def task_mg(request):
    if request.method == 'POST':
        requestobject = request.GET.get('TaskId')
        TaskData = Task.objects.get(id=requestobject)
        TaskData.estimated_end = request.POST.get('estimated_end')
        TaskData.startDate = request.POST.get('start_date')
        TaskData.save()
    project=Project.objects.all()
    return render(request, 'time.html',context={'pro':project})