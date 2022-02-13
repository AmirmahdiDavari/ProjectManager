from statistics import mode
from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from Project.models import Project, Sections, Category
from AddUser.models import MyUser
from django.utils.html import format_html


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
    model = Project


class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
    model = Project


class JSONEditor:
    pass


class ProjectAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'creator', 'jcreateDate', 'jstartDate', 'status', 'category')
    exclude = ['creator']
    search_fields = ('title', 'description')
    actions_on_top = False
    empty_value_display = 'وارد نشده ا ست '

    # project category
    def category(self, obj):
        return format_html(
            '<button class="rounded"><a class="btn primary-btn"      href=/admin/Project/category/?project_id__id__exact=' + str(
                obj.id) + ">دسته بندی</a></button>",
            obj
        )

    category.short_description = " دسته بندی  "

    # set user creator
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super().save_model(request, obj, form, change)

    def sections(self, obj):
        return format_html(
            "<button><a class='btn primary-btn' href=/admin/Step/step/?projectId="
            + str(obj.id) + ">بخش </a></button>", obj)

    # convert date to jalali_date
    def jcreateDate(self, obj):
        return date2jalali(obj.createDate)

    jcreateDate.short_description = "تاریخ ایجاد"

    # convert date to jalali_date
    def jstartDate(self, obj):
        return date2jalali(obj.startDate)

    jstartDate.short_description = "تاریخ شروع"


class SectionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'pid', 'status']
    actions_on_top = False


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tasks']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.GET:
            request = request.GET['_changelist_filters']
            request = request.split('=')[1]
            if db_field.name == "section_id":
                kwargs["queryset"] = Sections.objects.filter(projects__id=request)
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
    # set user creator

    def save_model(self, request, obj, form, change) -> None:
        if request.GET:
            request = request.GET['_changelist_filters']
            request = request.split('=')[1]
            obj.project_id = Project.objects.get(id=request)
            return super().save_model(request, obj, form, change)

    def tasks(self, obj):
        return format_html(
            "<button><a class='btn primary-btn'  href=/admin/Task/task/?category_id__id__exact=" + str(
                obj.id) + ">وظایف</a></button>",
            obj
        )

    tasks.short_description = 'تسک ها'


admin.site.register(Project, ProjectAdmin)
admin.site.register(Sections, SectionsAdmin)
admin.site.register(Category, CategoryAdmin)
