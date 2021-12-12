from django.contrib import admin

from .models import Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag','description','startDate')
    list_filter =['title','Experts']
    search_fields =('title','description')
    ordering =[ 'startDate','status']
    # action_form =
admin.site.register(Project, ProjectAdmin)
