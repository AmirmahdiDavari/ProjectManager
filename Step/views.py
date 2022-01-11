from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def steps(request,id):
    status,message,data=False,"خطا در api",""
    try:
        steps=Step.objects.filter(parent__isnull=True,projectId=id)
        steps=StepSerializer(steps,many=True).data
        message,data="مراحل پروژه ها با موفقیت بازگردانده شدند",steps
    except:
        message="مراحلی برای این پروژه یافت نشد"
    return response(status,message,data)