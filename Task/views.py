from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *



@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def updateTask(request,id):
    request=request.data
    status,message,data=False,"خطا در api",""

    # check status in request 
    if 'status' not in request :
        message="وضعیت تسک وارد نشده است"
    
    else:
        try:
            task = Task.objects.get(id=id)

            # set status
            if 'status' in request:
                task.status=request['status']

            # set endDate
            if 'estimatedEnd' in request:
                task.endDate=request['estimatedEnd']
            task.save()
            
            status,message,data=True,'تسک با موفقیت اپدیت شد',True

        except Task.DoesNotExist:
            message="چنین تسکی یافت نشد"
            
    return response(status,message,data)



@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def getTaskWithProjectId(request,id):
    status,message,data=False,"خطا در api",""
    
    try:
        task = Task.objects.filter(stepId__projectId=id)
        task=TaskSerializers(task,many=True)
        data=task.data
        status,message,data=True,'تسک ها بازگردانده شدند',data

    except Task.DoesNotExist:
        message="چنین تسکی یافت نشد"

    return response(status,message,data)

