from django.db import models
from AddUser.models import MyUser
from Project.models import Project


class parent(models.Model):


    class Meta:
        verbose_name = "والد"
        verbose_name_plural = 'لیست والد ها'


class Step(models.Model):
    SATTUS_Periority = {
        (1, 'high'),
        (2, 'normal'),
        (3, 'low')
    }
    name = models.CharField(max_length=200, verbose_name='عنوان')
    priority = models.IntegerField(verbose_name='اولویت')
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, verbose_name='ایدی پروژه',related_name="steps")
    parent = models.ForeignKey('self', verbose_name=("والد"), null=True,blank=True,on_delete=models.CASCADE)
    createDate=models.DateField("تاریخ ایجاد", auto_now_add=True)
    creator=models.ForeignKey(MyUser, verbose_name=("ایجاد کننده"),null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مرحله"
        verbose_name_plural = 'لیست مراحل'
