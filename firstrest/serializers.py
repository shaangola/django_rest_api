from rest_framework import serializers
from . models import Employee

class employeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields=('firstname' ,'lastname')
        fields='__all__'
