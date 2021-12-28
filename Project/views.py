from rest_framework.permissions import IsAuthenticated
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import ListProjecttSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
from jalali_date import datetime2jalali, date2jalali


class ProjectList(ListAPIView, LoginRequiredMixin):
    permission_classes = (IsAuthenticated,)

    serializer_class = ListProjecttSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Project.objects.all()
        else:
            return Project.objects.filter(Experts=self.request.user)


def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

# class ProjectVEWO(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, rquest, pk):
#         query = Project.objects.get(pk=pk)
#         serializer = updateProjecttSerializer(query)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         query = Project.objects.get(pk=pk)
#         serializer = updateProjecttSerializer(query, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
