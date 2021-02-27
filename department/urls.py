from django.urls import path
from .views import *
app_name = 'department'

urlpatterns = [
    path('<int:company_id>/', dashboard, name='dashboard'),
    path('create/<int:compid>/<int:f_id>', dashcreate, name='create'),
]
