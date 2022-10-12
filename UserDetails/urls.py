from django.urls import path
from .views import *

urlpatterns = [
    path('',home , name='home'),
    path('<int:emp_id>',show , name='show'),
    
]