from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from base.views import response
from Project.models import *


# from .models import project_scheduling
# def projectscheduling(request):
#     scheduling=project_scheduling.objects.all()
#     mydict={"time":scheduling}
#     return render(request,"scheduling.html",context=mydict)



# def my_view(request):
#     jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')