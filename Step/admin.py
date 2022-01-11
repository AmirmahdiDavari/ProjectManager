import re
from django.contrib import admin
from django.utils.html import format_html,mark_safe

from Project.models import Project
from .models import Step, parent

class StepAdmin(admin.ModelAdmin):
    list_filter=['projectId','name','creator']
    list_display=['name','projectId','tasks','steps']
    exclude=['projectId','creator']

    def get_queryset(self, request) :
        return super().get_queryset(request).filter(parent__isnull=True)


    # get steps of this project
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        request=request.GET['_changelist_filters']
        request=request.split('=')[1]
        if db_field.name == "parent":
            kwargs["queryset"] = Step.objects.filter(projectId=request,parent__isnull=True)
        return super(StepAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # get child steps
    def steps(self, obj):
        steps=Step.objects.filter(parent=obj.id)
        print(steps,obj.id)
        to_return = '<ul>'
        products = []
        for step in steps:
            products.append('<li><button><a href=/admin/Task/task/?stepId='+str(step.id)+'>'+step.name+'</a></button></li>')
            to_return = '<br/>'.join(products)
        return mark_safe(to_return)
    steps.short_description="زیر مراحل"

    def tasks(self,obj):
        return format_html(
            "<button><a href=/admin/Task/task/?stepId="+str(obj.id)+">تسک ها</a></button>"
        )
    tasks.short_description="تسک ها"

    def save_model(self, request, obj, form, change):
        request=request.GET['_changelist_filters']
        request=request.split('=')
        obj.creator=request.user
        obj.projectId=Project.objects.get(id=request[1])
        return super().save_model(request, obj, form, change)

admin.site.register(Step,StepAdmin)
admin.site.register(parent)
