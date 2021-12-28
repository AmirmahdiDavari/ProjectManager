from .models import Task
from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Task


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Task


class JSONEditor:
    pass


class TaskAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'Expert', 'jstartDate')
    list_filter = ['title', ]
    search_fields = ('title', 'description')
    ordering = ['status']

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


admin.site.register(Task, TaskAdmin)
