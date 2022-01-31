from unicodedata import name
from Project.models import Category, Sections
from Step.models import Step
from Task.models import Task
from django.contrib import admin
from jalali_date import date2jalali, datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from django.utils.html import format_html
from django.utils.datastructures import MultiValueDictKeyError
from urllib.parse import parse_qsl
from AddUser.models import MyUser
from django.utils.html import format_html
from Api.models import *
from Project.models import *


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Task


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Task


class JSONEditor:
    pass


class TaskAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):

    print ('dddddddddddddddd')
    # print(obj.name)

    list_display = ('title', 'description', 'get_createDate', 'get_startDate', 'expert', 'message', 'develop', 'validation')
    search_fields = ('title', 'description')

    # convert date to jalali date

    def get_createDate(self, obj):
        return date2jalali(obj.createDate)

    get_createDate.short_description = 'تاریخ ایجاد'

    # convert date to jalali date
    def get_startDate(self, obj):
        return date2jalali(obj.startDate)

    get_startDate.short_description = 'تاریخ شروع'

    # button link to add develop

    def message(self, obj):
        categoryItem = Category.objects.get(id =obj.category_id)

        if categoryItem.section_id_id== 8:  
            return format_html(
                "<button><a class='btn primary-btn'  href=/admin/Api/message/?task_id__id__exact=" + str(
                    obj.id) + ">پیام</a></button>",
                obj
            )

    message.short_description = 'پیام'

    # button link to add develop
    def develop(self, obj):
        categoryItem = Category.objects.get(id =obj.category_id)
        if categoryItem.section_id_id== 8:  
            return format_html(
                "<button><a class ='btn primary-btn' href =/admin/Api/develop/?task_id__id__exact=" + str(
                    obj.id) + "> توسعه</a></button>",
                obj
            )

    develop.short_description = 'توسعه '

    # button link to add validation
    def validation(self, obj):
        categoryItem = Category.objects.get(id =obj.category_id)
        if categoryItem.section_id_id== 8: 
            return format_html(
                "<button><a class ='btn primary-btn' href =/admin/Api/validation/?task_id__id__exact=" + str(
                    obj.id) + "> اعتبار سنجی </a></button>",
                obj
            )

    validation.short_description = "اعتبار سنجی "

    # save catgoriID & User_Creator ID in databise
    def save_model(self, request, obj, form, change) -> None:
        if request.GET:
            categoryId = request.GET['_changelist_filters']
            categoryId = categoryId.split('=')[1]
            obj.category = Category.objects.get(id=categoryId)
            obj.creator = request.user
            return super().save_model(request, obj, form, change)

    # /// motale shavad va  karbord moshakhas shavad
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if request.GET:
    #         request = request.GET['_changelist_filters']
    #         request = request.split('=')[1]
    #         if db_field.name == "Expert":
    #             kwargs["queryset"] = MyUser.objects.filter(projects__steps__id=request)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def save_model(self, request, obj, form, change) -> None:
    #     if request.GET:
    #         request = request.GET['_changelist_filters']
    #         request = request.split('=')[1]
    #         obj.task = Task.objects.get(id=request)
    #         return super().save_model(request, obj, form, change)


admin.site.register(Task, TaskAdmin)
