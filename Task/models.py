from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from AddUser.models import MyUser
# from jalali_date import datetime2jalali
from Project.models import *
from ProjectManager.settings import AUTH_USER_MODEL


# from Step.models import Step
# from extentions.Utils import jalali_converter


class Task(models.Model):
    STATUS_TASK = (
        (0, 'deActive'),
        (1, 'Active'),
        (2, 'Fail'),
        (3, 'Done'),
    )

    STATUS_RATE = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    }
    SATTUS_Periority = {
        (1, 'high'),
        (2, 'normal'),
        (3, 'low')
    }
    category = models.ForeignKey("Project.Category", verbose_name="دسته بندی", related_name='tasks', null=True,
                                 blank=True, on_delete=models.CASCADE,editable=False)
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    createDate = models.DateField(auto_now_add=True, editable=False, verbose_name='تاریخ ایجاد')
    startDate = models.DateField(blank=True, null=True, verbose_name='تاریخ شروع')
    creator = models.ForeignKey(MyUser, related_name="taskCreates", editable=False, null=True, blank=True,
                                verbose_name="ایجاد کننده",
                                on_delete=models.SET_NULL)
    status = models.IntegerField(choices=sorted(STATUS_TASK), default=0, blank=True, null=True, editable=False,
                                 verbose_name='وضعیت')
    expert = models.ForeignKey('AddUser.MyUser', on_delete=models.CASCADE,
                               null=True, verbose_name='کارشناس')
    periority = models.IntegerField(choices=sorted(SATTUS_Periority), default=3, verbose_name='الویت')
    ratePerformance = models.IntegerField(choices=sorted(STATUS_RATE), null=True, editable=False, verbose_name='امتیاز')
    doneDate = models.DateField(auto_now_add=True, )
    estimated_end = models.DateField(blank=True, null=True, editable=False, verbose_name='پایان تخمینی')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "تسک"
        verbose_name_plural = "لیست تسک ها"

    # def my_view(request):
    #     jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

    # def jstartDate(self):
    #     return jalali_converter(self.endDate)

    # jstartDate.short_description = "زمان انتشار"
