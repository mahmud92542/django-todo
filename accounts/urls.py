from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', login, name='login'),
    path('selcom/', selcom, name='selcom'),
    path('logout/', logout, name='logout'),
]
