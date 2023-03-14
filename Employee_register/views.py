from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):

    return render(request,'employee_register/home.html')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=UserCreationForm()

    return render(request,'employee_register/register.html',{'form':form})



def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect('employee_insert')
    else:
        form=AuthenticationForm()
    return render(request,'employee_register/login.html',{'form':form})


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id = 0):

    if request.method == 'POST':
        if id == 0:
            form = EmployeeForm()
            if form.is_valid():
                form.save()
                return redirect('employee_list')

        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
            if form.is_valid():
                form.save()
                return redirect('employee_list')



    else :
        if id == 0:
            form = EmployeeForm(request.GET)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})


def employee_delete( id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')
