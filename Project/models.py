from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from jalali_date import datetime2jalali, date2jalali
from AddUser.models import MyUser
from ProjectManager.settings import AUTH_USER_MODEL
from extentions.Utils import jalali_converter


class Sections(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام بخش")
    pid = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="زیرمجموعه")
    status = models.BooleanField(default=True, verbose_name="وضعیت")

    # class Meta:
    #     verbose_name = 'بخش '
    #     verbose_name_plural = 'بخش ها '

    def __str__(self):
        return self.name


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
    creator = models.ForeignKey(MyUser, related_name="projectCreates", null=True, blank=True,
                                verbose_name="ایجاد کننده", on_delete=models.CASCADE)
    createDate = models.DateField(auto_now_add=True)
    description = models.TextField(null=False, verbose_name="توضیحات")
    image = models.ImageField(upload_to='project/images', null=True, verbose_name="عکس")
    experts = models.ManyToManyField(AUTH_USER_MODEL, limit_choices_to={'groups__id': 1}, related_name="projects",
                                     verbose_name="کارشناس ها")
    scrumMaster = models.ManyToManyField(AUTH_USER_MODEL, limit_choices_to={'groups__id': 2},
                                         related_name="scrumasterProjects", verbose_name="اسکرام مستر")
    startDate = models.DateField(verbose_name="زمان شروع")
    endDate = models.DateField(verbose_name="زمان پایان")
    sections = models.ManyToManyField("Project.Sections", related_name="projects", 
                                      verbose_name="بخش ها")

    status = models.IntegerField(choices=sorted(STATUS_CHOICES), default=3, verbose_name="وضعیت", null=True, blank=True , editable=False)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = "لیست پروژه ها"

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html("<img width=100 height=75 src='{}'>".format(self.image.url))

    image_tag.short_description = "تصویر"


class Category(models.Model):
    STATUS_CATEGORY = (
        (0, 'Enable'),
        (1, 'Disable'),
    )
    name = models.CharField(max_length=100, verbose_name="عنوان")
    status = models.IntegerField(choices=sorted(STATUS_CATEGORY), verbose_name='وضعیت',default=0,editable=False)
    project_id = models.ForeignKey(Project, related_name='category', on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='شناسه پروژه')
    section_id = models.ForeignKey(Sections, related_name='category', on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='شناسه بخش')
    weight = models.IntegerField(verbose_name='وزن')

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها '

    def __str__(self):
        return self.name
    