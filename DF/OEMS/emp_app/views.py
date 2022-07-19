from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from emp_app.models import Employee

def index(request):
    return render(request, 'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    return render(request, 'view_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name = first_name, last_name = last_name, department_id = department, salary = salary,
        bonus = bonus, role_id = role, phone = phone, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!")
    elif request.method == "GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An exception occured employee could not be added!")

def remove_emp(request, emp_id=0):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    if emp_id:
        try:
            get_emp_id = Employee.objects.get(id = emp_id)
            get_emp_id.delete()
            return HttpResponse("Employee is removed successfully")
        except:
            return HttpResponse("Exception occurred")

    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name)|Q(last_name__icontains = name))
        if department:
            emps = emps.filter(department__name__icontains = department)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    
    else:
         return HttpResponse("Exception occured!")