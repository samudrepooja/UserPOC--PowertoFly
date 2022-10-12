from unittest.util import _MAX_LENGTH
from django.db import models

class UserData(models.Model):
    emp_id = models.AutoField(db_column='emp_id', primary_key=True)
    first_name = models.CharField(db_column='first_name',max_length = 100)
    last_name = models.CharField(db_column='last_name',max_length = 100)
    email = models.CharField(db_column='email',max_length = 100)
    department = models.CharField(db_column='department',max_length = 100)
    salary = models.IntegerField(db_column='salary')
    gender = models.CharField(db_column='gender',max_length = 100)
    class Meta:
        managed = True
        db_table = 'UserData'
