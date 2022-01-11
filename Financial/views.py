from rest_framework import permissions
import rest_framework
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,APIView, permission_classes
from rest_framework.viewsets import ViewSet
from base.views import response
from Project.models import *


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def financial(request):
    status,message,data=False,"خطا در api",""
    financial=request.user.userMoneydepositor
    financial=FinancialSerializer(financial,many=True).data
    message,data="پرداخت ها با موفقیت بازگردانده شدند",financial
    try:
        financial=request.user.userMoneydepositor
        financial=FinancialSerializer(financial,many=True).data
        message,data="پرداخت ها با موفقیت بازگردانده شدند",financial
    except Exception:
        message="پرداختی یافت نشد"
    return response(status,message,data)