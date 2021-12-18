from django.db import models
from Project.models import Project


class parent(models.Model):
    parentname = models.CharField(max_length=50, verbose_name='نام والد')

    def __str__(self):
        return self.parentname

    class Meta:
        verbose_name = "والد"
        verbose_name_plural = 'لیست والد ها'


class Step(models.Model):
    SATTUS_Periority = {
        (1, 'high'),
        (2, 'normal'),
        (3, 'low')
    }
    Name = models.CharField(max_length=200, verbose_name='عنوان')
    priority = models.IntegerField(verbose_name='اولویت')
    ProjectId = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, verbose_name='ایدی پروژه')
    Parent = models.OneToOneField(parent, on_delete=models.CASCADE, null=True, verbose_name='ایدی والد')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "مرحله"
        verbose_name_plural = 'لیست مراحل'
