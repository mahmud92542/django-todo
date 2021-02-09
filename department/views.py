from django.shortcuts import render
from .models import *
# dashboard page functionality...


def dashboard(request, company_id):
    company = Company.objects.get(id=company_id)
    department = CompanyDept.objects.filter(compid=company_id)
    compdept = CompanyDeptUser.objects.filter(
        user=request.user,
        compid=company
    )
    permission_department_list = []

    for dept in compdept:
        permission_department_list.append(dept.deptid.id)
    context = {
        'department': department,
        'compdept': compdept,
        'permission_department_list': permission_department_list
    }
    return render(request, 'departments/dashboard.html', context)


def dashcreate(request, f_id):
    if request.method == 'POST':
        return render(request, 'departments/dashcreate.html')
