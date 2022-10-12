from functools import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import UserData
from UserDetails import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .filters import EmployeeFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)
    
def get_user(filter_user = None):
    if filter_user:
        print("DATA COMING FROM DB")
        user = UserData.objects.filter(emp_id = filter_user)
    else:
        user = UserData.objects.all().order_by('emp_id')
    return user

def home(request):
    filter_user = request.GET.get('user')
    
    print("filter user value ----",filter_user)
    if cache.get(filter_user):
        print("DATA COMING FROM CACHE")
        user = cache.get(filter_user)
    else:  
        if filter_user:
            user = get_user(filter_user)
            cache.set(filter_user, user)
        else:
            user = get_user() 
    page_number = request.GET.get('page')
    if filter_user is None and page_number is not None :
        user = cache.get(filter_user)
        
    context = {}
    filtered_employee = EmployeeFilter(
        request.GET,
        queryset = user
    )
    context['filtered_employee'] = filtered_employee
    per_page = 1000
    paginated_filtered_employees = Paginator(filtered_employee.qs,per_page)#paginate by 2
    page_obj = paginated_filtered_employees.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'user/show_filtered_employee.html' , context)   

def show(request , emp_id):
    print("-------",emp_id)
    if cache.get(emp_id):
        print("DATA COMING FROM CACHE")
        user = cache.get(emp_id)
    else:
        print("DATA COMING FROM DB")
        print(cache)
        user = UserData.objects.get(emp_id = emp_id)
        cache.set(emp_id , user)
    context = {'user' : user}
    return render(request, 'user/show.html' , context)