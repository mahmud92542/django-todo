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
