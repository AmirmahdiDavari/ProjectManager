from .models import Task
from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from AddUser.models import MyUser

class TaskAdmin(admin.ModelAdmin, ModelAdminJalaliMixin):
    list_display = ('title', 'image_tag', 'description', 'jstartDate',)
    list_filter = ['title', 'Experts']
    search_fields = ('title', 'description')
    ordering = ['startDate', 'status']



class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Task


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Task


class JSONEditor:
    pass


class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


admin.site.register(Task, FirstModelAdmin)
