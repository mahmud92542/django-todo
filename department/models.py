from django.db import models
from django.db.models import DateTimeField
from django.contrib.auth import get_user_model
User = get_user_model()


# creating departments model and table with multiple attributes
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# creating company model and table with multiple attributes
class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# creating company_dept model and table with multiple attributes
class CompanyDept(models.Model):
    compid = models.ForeignKey(Company, on_delete=models.CASCADE)
    deptid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.compid)

# creating company_dept_user table with multiple attributes


class CompanyDeptUser(models.Model):
    compid = models.ForeignKey(Company, on_delete=models.CASCADE)
    deptid = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user)


STATUS = (
    ('wip', 'Work in progress'),
    ('done', 'Complete')
)

SSUBMIT = (
    ('approved', 'Approve'),
    ('wip', 'Not approved')
)

# creating works model and table with multiple attributes


class Work(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=50)
    exdate = models.DateTimeField(null=True, blank=True)
    remarks = models.CharField(max_length=50)
    reqno = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    ssubmit = models.CharField(choices=SSUBMIT, max_length=50)
    fapproval = models.CharField(max_length=50)
    po_wo = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    createdby = models.ForeignKey(
        User, related_name="user_who_create", on_delete=models.CASCADE, null=True, blank=True)
    createdon = models.DateTimeField(null=True, blank=True)
    updatedby = models.ForeignKey(
        User, related_name="user_who_update", on_delete=models.CASCADE, null=True, blank=True)
    updatedon = models.DateTimeField(null=True, blank=True)
    compid = models.ForeignKey(Company, on_delete=models.CASCADE)
    deptid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
