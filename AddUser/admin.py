from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MyUser


def _(param):
    pass


class MyUserAdmin(UserAdmin):
    model = MyUser
    # add_form = MyUserForm

    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','Skill')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
        (_('Important dates'), {'fields': ( 'date_joined',)}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2'),
    #     }),
    # )

    UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    UserAdmin.list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    UserAdmin.search_fields = ('username', 'first_name', 'last_name', 'email')


admin.site.register(MyUser, MyUserAdmin)
