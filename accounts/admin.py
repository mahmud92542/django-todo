from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission


admin.site.site_header = "OOMS ADMIN"


# User
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
        'groups_list', 'permissions'
    ]
    list_display_links = ['username']
    list_editable = ['is_active', 'is_staff', 'is_superuser']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ['username', 'first_name', 'last_name', 'email']
    filter_horizontal = ['groups', 'user_permissions']
    ordering = ['-id', 'username', ]

    def groups_list(self, obj):
        return " | ".join([i.name for i in obj.groups.all()])

    def permissions(self, obj):
        return " | ".join([i.codename for i in obj.user_permissions.all()])


# Group
admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'permissions_list']
    list_display_links = ['name']
    search_fields = ['name']
    filter_horizontal = ['permissions']
    ordering = ['-id']

    def permissions_list(self, obj):
        return " | ".join([i.codename for i in obj.permissions.all()])
