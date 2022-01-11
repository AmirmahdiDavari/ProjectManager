from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def projects(request):
    status,message,data=False,"خطا در api",""
    try:
        projects=request.user.projects
        projects=ProjectSerializer(projects,many=True).data
        message,data="پروژه ها با موفقیت بازگردانده شدند",projects
    except:
        message="چنین پروژه ای یافت نشد"
    return response(status,message,data)



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def projectMembers(request,id):
    status,message,data=False,"خطا در api",""
    try:
        project=Project.objects.get(id=id)
        experts=UserSerializer(project.experts,many=True).data
        scrumMaster=UserSerializer(project.scrumMaster,many=True).data
        message,data="کارشناسان و اسکرامستر پروژه با موفقیت بازگردانده شدند",{'scrumMaster':scrumMaster,'experts':experts}
    except:
        message="چنین پروژه ای یافت نشد"
    return response(status,message,data)
