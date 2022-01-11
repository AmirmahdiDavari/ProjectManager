from Step.models import Step
from .models import Task
from django.contrib import admin
from jalali_date import date2jalali, datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from django.utils.html import format_html
from AddUser.models import MyUser
class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Task


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Task


class JSONEditor:
    pass


class TaskAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'description','get_createDate' ,'get_startDate','status', 'expert')
    exclude=['stepId','endDate','creator']
    search_fields = ('title', 'description')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        request=request.GET['_changelist_filters']
        request=request.split('=')[1]
        if db_field.name == "expert":
            kwargs["queryset"] = MyUser.objects.filter(projects__steps__id=request)
        return super(TaskAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


    def save_model(self, request, obj, form, change):
        request=request.GET['_changelist_filters']
        request=request.split('=')
        obj.creator=request.user
        obj.stepId=Step.objects.get(id=request[1])
        return super().save_model(request, obj, form, change)
   
    def get_createDate(self, obj):
        return date2jalali(obj.createDate)

    get_createDate.short_description = 'تاریخ ایجاد'

    def get_startDate(self, obj):
        return date2jalali(obj.startDate)

    get_startDate.short_description = 'تاریخ شروع'


admin.site.register(Task, TaskAdmin)
