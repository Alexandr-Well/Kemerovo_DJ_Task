from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin, Group
from .models import CustomUser, CustomGroup


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'fathers_name',
        'verification',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'fathers_name', 'email', 'birthday')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'verification',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )


class CustomGroupAdmin(GroupAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.unregister(Group)
