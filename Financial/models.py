from django.db import models
from Project.models import Project
from django.contrib.auth.models import User
from extentions.Utils import jalali_converter

from ProjectManager import settings


class financial(models.Model):
    STATUS_TYPE = {
        (1, 'واریز '),
        (2, ' برداشت'),
    }

    title = models.CharField(max_length=50, verbose_name="عنوان")
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="ایدی پروژه")
    Date = models.DateField(auto_now=True, verbose_name="تاریخ واریز")
    Description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='images', null=True, verbose_name="عکس")
    type = models.IntegerField(choices=sorted(STATUS_TYPE), verbose_name="نوع")
    money = models.CharField(max_length=50, verbose_name="پول")
    userRecipientofmoney = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='userMoneydepositor',
                                                  verbose_name="دریافت کننده")
    userMoneydepositor = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="پرداخت کننده")

    def __str__(self):
        return self.title

    def jstartDate(self):
        return jalali_converter(self.Date)

    jstartDate.short_description = "تاریخ واریز"

    class Meta:
        verbose_name = "مالی"
        verbose_name_plural = "لیست مالی"
