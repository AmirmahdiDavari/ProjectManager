from django.contrib import admin
from django.forms import JSONField
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from extentions.Utils import jalali_converter
from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import Project
class ProjectAdmin(admin.ModelAdmin,ModelAdminJalaliMixin):
    list_display = ('title','image_tag','description','jstartDate',)
    list_filter =['title','Experts']
    search_fields =('title','description')
    ordering =[ 'startDate','status']





class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Project


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Project


class JSONEditor:
    pass


class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    # list_display = ['some_fields', 'get_created_jalali']
    #
    # inlines = (MyInlines1, MyInlines2,)
    # raw_id_fields = ('some_fields',)
    # readonly_fields = ('some_fields', 'date_field',)
    # # you can override formfield, for example:
    # formfield_overrides = {
    #     JSONField: {'widget': JSONEditor},
    # }

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'




admin.site.register(Project,FirstModelAdmin)
