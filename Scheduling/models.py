from django.contrib.auth.models import User
from AddUser.models import MyUser
from Project.models import Project
from django.db import models
from django.contrib.auth.models import User
from jalali_date import datetime2jalali, date2jalali
from AddUser.models import MyUser
from ProjectManager.settings import AUTH_USER_MODEL
from extentions.Utils import jalali_converter


class project_scheduling(models.Model):
    STATUS = (
        (1, 'Active'),
        (2, 'DeActive')
    )
    project_id = models.ForeignKey(Project, related_name='id_Project', on_delete=models.CASCADE,
                                   verbose_name="نام پروژه",null=True)
    user_id = models.ForeignKey(AUTH_USER_MODEL,
                                on_delete=models.CASCADE, verbose_name="نام کاربر",null=True)
    data = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    status = models.IntegerField(choices=sorted(STATUS), verbose_name="وضعیت",null=True)

    class Meta:
        verbose_name = 'نام پروژه'
        verbose_name_plural = "لیست زمانبندی پروژه  "

    def __int__(self):
        return self.status

    def jDate(self):
        return jalali_converter(self.data)

    jDate.short_description = "تاریخ"

    # def my_view(request):
    #     jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

