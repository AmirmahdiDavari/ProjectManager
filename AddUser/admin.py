from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MyUser


def _(param):
    pass


class MyUserAdmin(UserAdmin):
    model = MyUser

    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )
    UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','get_groups')
    UserAdmin.list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    UserAdmin.search_fields = ('username', 'first_name', 'last_name', 'email')

    def get_groups(self,queri):
        return str(tuple(queri.groups.values_list('name',flat=True)))



    get_groups.short_description = 'گروه'


admin.site.register(MyUser, MyUserAdmin)
