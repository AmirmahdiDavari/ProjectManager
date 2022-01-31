from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
# from django.utils.generic import ListView  
from django.views.generic.list import ListView
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *
from rest_framework.views import APIView
from rest_framework.response import Response



@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def updateTask(request, id):
    request = request.data
    status, message, data = False, "خطا در api", ""

    # check status in request
    # if 'status' not in request:
    #     message = "وضعیت تسک وارد نشده است"

    # else:
    try:
        task = Task.objects.get(id=id)
        # set endDate
        if request['field'] == "estimatedEnd":
            task.estimated_end = request['value']

        # # set status
        if request['field'] == 'status':
            task.status = request['value']

        # if 'estimatedEnd' in request:
        #     task.endDate = request['estimatedEnd']
        task.save()

        status, message, data = True, 'تسک با موفقیت اپدیت شد', True

    except Task.DoesNotExist:
        message = "چنین تسکی یافت نشد"

    return response(status, message, data)


# @api_view(["GET"])
# @permission_classes([permissions.IsAuthenticated])
# def getTaskWithProjectId(request, id):
#     status, message, data = False, "خطا در api", ""

#     try:
#         task = Task.objects.filter(stepId__projectId=id)
#         task = TaskSerializers(task, many=True)
#         data = task.data
#         status, message, data = True, 'تسک ها بازگردانده شدند', data

#     except Task.DoesNotExist:
#         message = "چنین تسکی یافت نشد"

#     return response(status, message, data)
class TaskList(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self,request):
        status, message, data = False, "خطا در api", ""
        try:
            task = Task.objects.all()
            taskserilazer = TaskSerializers(task, many=True)
            data = taskserilazer.data
            status, message, data = True, 'تسک ها بازگردانده شدند', data
        except:
            message = "چنین تسکی یافت نشد"
        return response(status, message, data)


    def post (self,request):
        
        status, message, data = False, "خطا در api", ""
        return response(status, "تست post", data)



class TaskDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get (self,request,id):
                
        status, message, data = False, "خطا در api", ""

        try:
            task = Task.objects.filter(stepId__projectId=id)
            taskserilazer = TaskSerializers(task, many=True)
            data = taskserilazer.data
            status, message, data = True, 'تسک ها بازگردانده شدند', data
        except:
            message = "چنین تسکی یافت نشد"
        return response(status, message, data)


    def post (self,request,id):
        
        status, message, data = False, "خطا در api", ""
        return response(status, "تست post", data)



class task_project(ListView):
    model=Task
    template_name='Task.html'


class task_detile(ListView):
    model=Task
    template_name='Task_detile.html'
