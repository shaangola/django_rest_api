from rest_framework import serializers
from . models import Employee
from paymateweb.models import *


class employeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields=('firstname' ,'lastname')
        fields='__all__'


class userSerializers():
    class Meta:
        model=Users
        fields=('fname','lname')
        fields='__all__'


