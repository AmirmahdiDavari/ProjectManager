from django.contrib import admin
from Task.models import Task
from Api.models import Attach, Validation, Develop, Testing, Message
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


# ___________________________________________________Admin_Attach___________________________________________________
class Admin_Attach(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('TYPE', 'name', 'path',)
    exclude = ['creator_id']

    # set user creator
    def save_model(self, request, obj, form, change):
        obj.creator_id = request.user
        return super(Admin_Attach, self).save_model(request, obj, form, change)


# ___________________________________________________Admin_Message___________________________________________________
class Admin_Message(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'code', 'status')
    exclude = ['creator_id', "task_id"]
    actions_on_top = False
    actions_selection_counter = False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.GET:
            request = request.GET['_changelist_filters']
            request = request.split('=')[1]
            if db_field.name == "task_id":
                kwargs["queryset"] = Task.objects.filter(Task__id=request)
                return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # save taskID & User_Creator ID in databise

    def save_model(self, request, obj, form, change) -> None:
        if request.GET:
            TaskID = request.GET['_changelist_filters']
            TaskId = TaskID.split('=')[1]
            obj.task_id = Task.objects.get(id=TaskId)
            obj.creator_id = request.user
            return super().save_model(request, obj, form, change)


# ___________________________________________________Admin_Validation___________________________________________________

class Admin_Validation(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'status',)
    exclude = ['creator_id','task_id',]
    actions_on_top = False

    # save catgoriID & User_Creator ID in databise
    def save_model(self, request, obj, form, change) -> None:
        if request.GET:
            TaskID = request.GET['_changelist_filters']
            TaskId = TaskID.split('=')[1]
            obj.task_id = Task.objects.get(id=TaskId)
            obj.creator_id = request.user
            return super().save_model(request, obj, form, change)


# ___________________________________________________Admin_Develop___________________________________________________

class Admin_Develop(ModelAdminJalaliMixin, admin.ModelAdmin):
    # list_display = ('method','name','url')
    exclude = ['creator_uid', "task_id"]
    actions_on_top = False

    # show  in list in panel
    def form_field_for_foreignkey(self, db_field, request, **kwargs):
        if request.GET:
            request = request.GET['_changelist_filters']
            request = request.split('=')[1]
            if db_field.name == "task_id":
                kwargs["queryset"] = Task.objects.filter(Task__id=request)
                return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # save taskID & User_Creator ID in database
    def save_model(self, request, obj, form, change) -> None:
        if request.GET:
            TaskID = request.GET['_changelist_filters']
            TaskId = TaskID.split('=')[1]
            obj.task_id = Task.objects.get(id=TaskId)
            obj.creator_uid = request.user
            return super().save_model(request, obj, form, change)


# ___________________________________________________Admin_Testing___________________________________________________

class Admin_Testing(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass


admin.site.register(Attach, Admin_Attach)
admin.site.register(Message, Admin_Message)
admin.site.register(Validation, Admin_Validation)
admin.site.register(Develop, Admin_Develop)
admin.site.register(Testing, Admin_Testing)
