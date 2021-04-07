from django.contrib import admin
from .models import *


class CompanyDeptUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'compid', 'deptid', 'user']


@admin.register(CompanyDept)
class CompanyDeptAdmin(admin.ModelAdmin):
    list_display = ['id', 'compid', 'deptid']
    list_display_links = ['id']
    list_filter = ['compid', 'deptid']
    ordering = ['-id']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'createdby', 'updatedby', 'compid', 'deptid']
    list_display_links = ['title']
    list_filter = ['compid', 'deptid', 'createdby', 'updatedby']
    ordering = ['-id']


admin.site.register(Department)
admin.site.register(Company)
admin.site.register(CompanyDeptUser, CompanyDeptUserAdmin)
