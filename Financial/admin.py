from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from jalali_date import datetime2jalali, date2jalali
from django.contrib import admin
from .models import financial

#
# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
#     model = financial
#
#
# class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
#     model = financial


class JSONEditor:
    pass


class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'Description', 'jstartDate', 'type', 'project_id')
    search_fields = ('title', 'Description')
    exclude = ['creator_financial']
    actions_on_top = False

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    def save_model(self, request, obj, form, change):
        obj.creator_financial = request.user
        return super().save_model(request, obj, form, change)

    get_created_jalali.short_description = 'تاریخ پرداخت'
    get_created_jalali.admin_order_field = 'created'


admin.site.register(financial, FirstModelAdmin)
