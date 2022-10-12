import django_filters
from  .models import UserData

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = UserData
        fields = '__all__'