from .models import financial

from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = financial


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = financial


class JSONEditor:
    pass


class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'Description', 'jstartDate', 'type')
    list_filter = ['title']
    search_fields = ('title', 'Description')

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ پرداخ'
    get_created_jalali.admin_order_field = 'created'


admin.site.register(financial, FirstModelAdmin)
