from django.shortcuts import get_object_or_404 
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee , many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT' , 'DELETE'])
def employee_detail(request,id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request) 
        employee_serializer = EmployeeSerializer(employee, data=employee_data) 
        if employee_serializer.is_valid(): 
            employee_serializer.save() 
            return JsonResponse(employee_serializer.data) 
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)