from django.urls import path
from .views import *
app_name = 'department'

urlpatterns = [
    path('<int:company_id>/', dashboard, name='dashboard'),
    path('create/<int:compid>/<int:f_id>', dashcreate, name='create'),

    # test route (filter)
    path('filter/<int:company_id>/', filter_view, name='filter_view'),

]
