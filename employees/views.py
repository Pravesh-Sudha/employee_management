from django.shortcuts import render, redirect
from .models import Employee

# List all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# Add new employee
def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        job_title = request.POST['job_title']
        Employee.objects.create(name=name, job_title=job_title)
        return redirect('employee_list')
    return render(request, 'employees/add_employee.html')

# Delete employee
def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')
