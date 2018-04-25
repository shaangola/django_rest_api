from django.contrib import admin
from . models import Employee
from paymateweb.models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Users)
