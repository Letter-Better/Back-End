from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import (User, Friend, Status)
from .forms import (ChangeUserForm, CreateUserForm)

class UserAdmin(BaseUserAdmin):
    form = ChangeUserForm
    add_form = CreateUserForm

    list_display = ('username', 'email', 'role')
    list_filter = ('role',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('info', {'fields': ('full_name',)}),
        ('Perms', {'fields': ('role',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', '_password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Friend)
admin.site.register(Status)
