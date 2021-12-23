from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from .models import Project
from AddUser.models import MyUser


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Project


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Project


class JSONEditor:
    pass


class end_date(Project):
    def enddate(self):
        if Project.status == 1:
            Project.endDate = True
        elif Project.status == 2:
            Project.endDate = True
        else:
            Project.endDate = False


class ProjrctAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'description', 'jstartDate', 'status')
    list_filter = ['title', 'Experts']
    search_fields = ('title', 'description')
    ordering = ['startDate', 'status']
    actions_on_top = False
    actions_selection_counter = True
    empty_value_display = 'وارد نشده ا ست '

    # radio_fields = {"group": admin.VERTICAL}
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "Expert":
            kwargs["queryset"] = MyUser.objects.filter(Expert__in=1)
        return super(ProjrctAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "myuser":
            kwargs["queryset"] = MyUser.objects.filter(Role=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Meta:
        def enddate(self):
            if Project.status == 1:
                Project.endDate = True
            elif Project.status == 2:
                Project.endDate = True
            else:
                Project.endDate = False


admin.site.register(Project, ProjrctAdmin)

# class BucketAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "things":
#              kwargs["queryset"] = Things.objects.filter(...)
#         return super(BucketAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
