from pprint import pprint
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# dashboard page functionality...


@login_required
# def dashboard(request, company_id):
def dashboard(request, **kwargs):
    # company = Company.objects.get(id=company_id)
    company = Company.objects.get(id=kwargs['company_id'])
    # department = CompanyDept.objects.filter(compid=company_id)
    department = CompanyDept.objects.filter(compid=kwargs['company_id'])

    # debug
    queryset = Work.objects.filter(compid=kwargs['company_id'])

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
        'permission_department_list': permission_department_list,

        # debug
        'queryset': queryset
    }
    return render(request, 'departments/dashboard.html', context)


# @login_required
@method_decorator(csrf_exempt, name='dispatch')
def dashcreate(request, compid, f_id):
    # print('compid: ', compid)
    # print('f_id: ', f_id)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        print('49', title, description)

        # print('if')
        # print('title', request.POST.get('title'))
        # print('description', request.POST.get('description'))
        # print('status', request.POST.get('status'))
        # print('remarks', request.POST.get('remarks'))
        # print('createdby', request.POST.get('createdby'))

        # fields = ['title', 'description', 'status', 'remarks', 'createdby']

        form = WorkForm(data=request.POST)
        pprint(form)
        print(form.is_valid())
        # print(form.cleaned_data['title'])

        company = Company.objects.get(id=compid)
        # print('company: ', company)

        department = Department.objects.get(id=f_id)
        # print('department: ', department)

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


# test view: path('filter/<int:company_id>/', filter_view, name='filter_view'),
@method_decorator(csrf_exempt, name='dispatch')
def filter_view(request, *args, **kwargs):
    queryset = Work.objects.filter(compid=kwargs['company_id'])
    print(queryset)
    template = 'departments/filtered_data.html'
    context = {'queryset': queryset}
    return render(request, template, context)
