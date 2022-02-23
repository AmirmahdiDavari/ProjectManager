from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from django.views.generic.list import ListView
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def updateTask(request, id):
    request = request.data
    status, message, data = False, "خطا در api", ""

    # check status in request
    # if 'status' not in request:
    #     message = "وضعیت تسک وارد نشده است"
    #
    # else:
    try:
        task = Task.objects.get(id=id)
        # set endDate
        if request['field'] == "estimatedEnd":
            task.estimated_end = request['value']
        # # set status
        if request['field'] == 'status':
            task.status = request['value']

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
            print('jjjjjjjjjjj')
            category = Category.objects.filter(project_id=id)
            task = Task.objects.filter(category_id__in=category)
            print(task)
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
    permission_classes =(IsAuthenticated,)
    template_name='Task.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        else:
            return Task.objects.filter(expert=self.request.user)

class task_detile(ListView):
    permission_classes=(IsAuthenticated,)
    template_name='Task_detile.html'

#     def form_field_for_foreignkey(self, request):
#         if request.GET:
#             request = request.GET['_changelist_filters']
#
#
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             qs=Task.objects.all()
#             return (qs)
#         else:
#             qs=Task.objects.get(project_id=request)
#
#             return Task.objects.filter(expert=self.request.user)


    def get_queryset(self):
        request = self.request.GET
        print(request)
        if self.request.method == 'GET':
            if self.request.user.is_superuser:
                request=request['projectId']

                queryset = Task.objects.filter(category__project_id__id=request)

                return queryset
            else:
                request=request['projectId']
                print(request)

                queryset= Task.objects.filter(category__project_id__id=request,expert=self.request.user)

                return queryset

class Dashbord(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self,request):
        status, message, data = False, "خطا در api", ""
        if request.GET:
            request = request.GET['type']
            if request == '1' :
                print('11111')
                task = Task.objects.filter(expert=self.request.user,estimated_end__isnull=True)
                dashbord = DashbordTasktSerializer(task, many=True)
                data = dashbord.data
                status, message, data = True, 'تسک ها بازگردانده شدند', data
            elif request == '2' :
                task = Task.objects.filter(expert=self.request.user,status=1)
                dashbord = DashbordTasktSerializer(task, many=True)
                data = dashbord.data
                status, message, data = True, 'تسک ها بازگردانده شدند', data
            elif request == '3':
                task = Task.objects.filter(expert=self.request.user,estimated_end__lte = datetime.now())
                dashbord = DashbordTasktSerializer(task, many=True)
                data = dashbord.data
                status, message, data = True, 'تسک ها بازگردانده شدند', data
            else:
                status, message, data = False, '  چنین تسکی یافت نشد ', {}
        return response(status, message, data)

