from rest_framework import permissions
import rest_framework
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.decorators import api_view,APIView, permission_classes
from rest_framework.viewsets import ViewSet
from base.views import response
from Project.models import *


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def financial(request):
#     status,message,data=False,"خطا در api"," "
#     try:
#         financial=request.user.userMoneydepositor
        

       

#         financials=FinancialSerializer(financial,many=True)
#         print(len (financials.data))
        
#         data=financials.data
#         if data.is_valid==False:
#             message,data,status="پرداخ شدند"," ",False
#         message,data,status="پرداخت ها با موفقیت بازگردانده شدند",data,True

#     except :
#         message ="پرداخت ها با موفقیت بازگردانده شدند"

#     return response(status,message,data)
# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def financial(request):
#     status,message,data=False,"خطا در api"," "
#     try:
#         financial=request.user.userMoneydepositor
#         financials=FinancialSerializer(financial,many=True)
#         data=financials.data
#         if len(data) >0:
#             message, data, status = " ها با موفقیت بازگردانده شدند", data, True
#         else :
#             message , data , status = "پرداختی وجود ندارد " , "" , False

#     except :
#         pass
#         # message , data , status = "test" , "" , False
#     return response(status,message,data)


class FinancialList(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self,request):
        status, message, data = False, "خطا در api", ""
        try:
            financial=request.user.userMoneydepositor
            financials=FinancialSerializer(financial,many=True)
            data=financials.data
            if not data:
                return response (" صورتحساب مالی یافت نشد", " ", False)
            message,status,data="صورتحساب مالی با موفقیت بازگردانده شد ",True,data
            
            
        except:
            pass
        return response(status, message, data)
