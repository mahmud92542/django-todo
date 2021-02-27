from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# dashboard page functionality...


@login_required
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

    for d in department:
        print(d.deptid.id)
    print(permission_department_list)

    context = {
        'department': department,
        'compdept': compdept,
        'permission_department_list': permission_department_list
    }
    return render(request, 'departments/dashboard.html', context)


@login_required
def dashcreate(request, compid, f_id):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        company = Company.objects.get(id=compid)
        department = Department.objects.get(id=f_id)
        if form.is_valid():
            work = form.save(commit=False)
            work.createdby = request.user
            work.compid = company
            work.deptid = department
            work.save()
            return redirect('department:dashboard', company_id=compid)
    else:
        form = WorkForm()
        return render(request,'departments/dashcreate.html',{'form':form})
