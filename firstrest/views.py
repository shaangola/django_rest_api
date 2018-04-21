from django.shortcuts import render


from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serializers import employeeSerializers

# Create your views here.
class employeeList(APIView):

    def get(self,request):
        employeedata = Employee.objects.all()
        serializer = employeeSerializers(employeedata,many=True)
        return Response(serializer.data)

    def post(self):
        pass
