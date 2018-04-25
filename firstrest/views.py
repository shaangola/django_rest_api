from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import *
from paymateweb.models import Users

# Create your views here.
class employeeList(APIView):

    def get(self,request):
        employeedata = Employee.objects.all()
        serializer = employeeSerializers(employeedata,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class userList(APIView):
    def get(self,request):
        userlist = Users.objects.all()
        serializer = userSerializers(userlist,many = True)
        return Response(serializer.data)



