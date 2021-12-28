from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import project_scheduling


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = project_scheduling


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = project_scheduling


class JSONEditor:
    pass


class ScrumMasterAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user_id', 'project_id', 'status', 'jDate')

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'


#     def get_queryset(self, request):
#         return super(ScrumMasterAdmin,self).get_queryset(request).filter(Project.models.Project.Experts=request.user.id)


admin.site.register(project_scheduling, ScrumMasterAdmin)
