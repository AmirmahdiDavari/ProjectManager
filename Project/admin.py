from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import Project
from AddUser.models import MyUser
from django.utils.html import format_html

class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Project


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Project


class JSONEditor:
    pass


class ProjrctAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'creator', 'jcreateDate','jstartDate', 'status','steps')
    exclude=['creator']
    # list_filter = ['title', 'Experts']
    search_fields = ('title', 'description')
    # ordering = ['jstartDate', 'status']
    actions_on_top = False
    actions_selection_counter = True
    empty_value_display = 'وارد نشده ا ست '


    # project steps
    def steps(self,obj):
        return format_html(
            "<button><a class='btn primary-btn' href=/admin/Step/step/?projectId="+str(obj.id)+">مراحل</a></button>",
            obj
        )
    steps.short_description="مراحل"
    
    # set user creator
    def save_model(self, request, obj, form, change) :
        obj.creator=request.user
        return super().save_model(request, obj, form, change)


    # createDate
    def jcreateDate(self,obj):
        return date2jalali(obj.createDate)
    jcreateDate.short_description="تاریخ ایجاد"
    # startDate
    def jstartDate(self,obj):
        return date2jalali(obj.startDate)
    jstartDate.short_description="تاریخ شروع"


admin.site.register(Project, ProjrctAdmin)
