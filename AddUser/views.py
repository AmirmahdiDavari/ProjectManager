from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,APIView, permission_classes
from rest_framework import permissions
import random
from .serializers import UserSerializer
from .jwt import get_tokens_for_user
from base.views import response
from AddUser.models import MyUser
from .forms import *
import datetime
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
@permission_classes([permissions.AllowAny])

# login with phone
def loginPhone(request):
    status,message,data = False,"",{}
    return response(False,'این متد هنوز فعال نشده است ','')

    request=request.data

    if 'phone' not in request:
        return response(False,'شماره تماس را وارد کنید ',request)
    
    user=MyUser.objects.filter(phone=request['phone']).first()

    # برای سریالایزر کردن استافده میشه
    # user=MyUserSerializers(user,many=False)
    # return response(False,'شماره تماس را وارد کنید ',user.data,200)
    
    # کاربر موجود بود
    if user:
        # گرفتن زمان حاضر و زمان اعتبار کد احراز هویت
        userTime=user.codeTime.timestamp()+120
        currentTime=datetime.datetime.now().timestamp()

        # کد در درخواست موجود بود
        if 'code' in request:
            
            # کد اعتبار داشت
            if userTime >= currentTime :

                # کد صحیح بود
                if request['code']==user.code:
                    status,message,data=True,"توکن کاربر با موفقیت بازگشت داده شد",get_tokens_for_user(user)

                # کد صحیح نبود
                elif request['code']!=user.code:
                    status,message,data=False,"کد وارد شده صحیح نمیباشد",[]

            # کد اعتبار نداشت
            elif userTime < currentTime :
                code=random.randint(100000,999999)
                user.code=code
                user.codeTime=datetime.datetime.now()
                user.save()
                #  در این قسمت باید ارسال پیامک را داشته باشیم
                status,message,data=True,"کد احراز هویت با موفقیت ارسال شد",[]


        # کد در درخواست موجود نبود
        else:
            if userTime >= currentTime :
                status,message,data=False,"کد قبلی همجنان معتبر است",[]

            else:   
                code=random.randint(100000,999999)
                user.code=code
                user.codeTime=datetime.datetime.now()
                user.save()
                # در این قسمت باید ارسال پیامک را داشته باشیم
                status,message,data=True,"کد احراز هویت با موفقیت ارسال شد",[]

    # کاربر با این شماره تماس موجود نبود
    else:
        code=random.randint(100000,999999)
        user=MyUser(phone=request['phone'],name=request['phone'],code=code,codeTime=datetime.datetime.now())
        user.save()
        #  در این قسمت باید ارسال پیامک را داشته باشیم
        status,message,data=True,"کاربر ایجاد شد و کد احراز هویت ارسال شد",[]

        
    return response(status,message,data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
# login with email
def loginEmail(request):
    status,message,data = False,"",""
    request=request.data


    # validation
    validation=emailLoginValidation(request)
    if not validation.is_valid():
        return response(status,"اطلاعات ورودی صحیح نمیباشد",validation.errors.as_data())

    # get user model
    user=MyUser.objects.filter(email=request['email']).first()
    
    # check user password
    try:
        user.check_password(request['password'])
        status,message,data=True,'کاربر با موفقیت وارد شد',get_tokens_for_user(user)
    except:
        message='گذر واژه وارد شده صحیح نمیباشد'
            
    return response(status,message,data)



@api_view(['POST','GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    user=request.user
    user=UserSerializer(user,many=False)
    return response(True,"اطلاعات کاربر بازگردانده شد",user.data)
