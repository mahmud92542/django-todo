from django.contrib import admin
from .models import *


class CompanyDeptUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'compid', 'deptid', 'user']


admin.site.register(Department)
admin.site.register(Work)
admin.site.register(Company)
admin.site.register(CompanyDept)
admin.site.register(CompanyDeptUser, CompanyDeptUserAdmin)
