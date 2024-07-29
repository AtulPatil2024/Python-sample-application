from rest_framework import serializers 
from Employee.models import Employee
 
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id','firstName','lastName','emailId')