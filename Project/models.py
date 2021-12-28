from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from jalali_date import datetime2jalali, date2jalali
from AddUser.models import MyUser
from ProjectManager.settings import AUTH_USER_MODEL
from extentions.Utils import jalali_converter


class Project(models.Model):

    def test_validator(self):
        if self.Role == '1':
            return self

    STATUS_CHOICES = {
        (1, 'Done'),
        (2, 'deActive'),
        (3, 'Active'),
        (4, 'Fail'),
    }

    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(null=False, verbose_name="توضیحات")
    image = models.ImageField(upload_to='images', null=True, verbose_name="عکس")
    Experts = models.ManyToManyField(AUTH_USER_MODEL, limit_choices_to={'groups__name': "Expert"},
                                     related_name="creator_set", verbose_name="کارشناس ها")
    ScrumMaster = models.ManyToManyField(AUTH_USER_MODEL, limit_choices_to={'groups__name': "ScrumMaster"},
                                         verbose_name="اسکرام مستر")
    startDate = models.DateField(verbose_name="زمان شروع")
    endDate = models.DateField(verbose_name="زمان پایان")
    status = models.IntegerField(choices=sorted(STATUS_CHOICES), default=2, verbose_name="وضعیت", null=True, blank=True)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = "لیست پروژه ها"

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html("<img width=100 height=75 src='{}'>".format(self.image.url))

    image_tag.short_description = "عکس"

    def jstartDate(self):
        return jalali_converter(self.startDate)

    jstartDate.short_description = "زمان انتشار"

    def my_view(request):
        jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
