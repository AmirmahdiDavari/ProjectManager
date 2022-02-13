from rest_framework import permissions
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from django.views.generic.list import ListView
from Project.models import *
from Project.serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *
from rest_framework.views import APIView


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def projects(request):
#     status, message, data = False, "خطا در api", ""
#     try:
#         projects = request.user.projects
#         projects = ProjectSerializer(projects, many=True).data
#         message, data,status = "پروژه ها با موفقیت بازگردانده شدند", projects,True
#     except:
#         message = "چنین پروژه ای یافت نشد"
#     return response(status, message, data)


# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def projectMembers(request, id):
#     status, message, data = False, "خطا در api", ""

#     try:
#         project = Project.objects.get(id=id)
#         experts = UserSerializer(project.experts, many=True).data
#         scrumMaster = UserSerializer(project.scrumMaster, many=True).data

#         message, data, status = "کارشناسان و اسکرامستر پروژه با موفقیت بازگردانده شدند", {'scrumMaster': scrumMaster,
#                                                                                           'experts': experts},True

#     except:
#         message = "چنین پروژه ای یافت نشد"
#     return response(status, message, data)
class ProjectList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        status, message, data = False, "خطا در api", " "
        try:
            project=Project.objects.all()
            # projects = request.user.projects
            serializers = ProjectSerializer(project, many=True).data
            message, data, status = "پروژه ها با موفقیت بازگردانده شدند", serializers, True
        except:
            message = "چنین پروژه ای یافت نشد"
        return response(status, message, data)


class ProjectMembers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        status, message, data = False, "خطا در api", " "
        try:
            project = Project.objects.get(id=id)
            experts = UserSerializer(project.experts, many=True).data
            scrumMaster = UserSerializer(project.scrumMaster, many=True).data
            message, data, status = "کارشناسان و اسکرامستر پروژه با موفقیت بازگردانده شدند", {
                'scrumMaster': scrumMaster,
                'experts': experts}, True
        except:
            message = "چنین پروژه ای یافت نشد"
        return response(status, message, data)


class list_project(ListView):
    permission_classes = (IsAuthenticated,)
    template_name = "project.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Project.objects.all()
        else:
            return Project.objects.filter(experts=self.request.user)




def handler403(request, exception):
    return render(request, '403.html', status=403)


def handler500(request):
    return render(request, 'error/500.html', status=500)


def handler404(request, exception):
    return render(request, '404.html', status=404)

