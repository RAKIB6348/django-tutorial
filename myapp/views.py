from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def homepage(request):
    return render(request, 'master.html')


def student_page(request):
    students = StudentModel.objects.all()
    return render(request, 'student/student.html', {'students' : students})


def add_student_page(request):
    departments = DepartmentModel.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        department = request.POST.get('department')

        if firstname and lastname and department:
            department = DepartmentModel.objects.get(id=department)

        StudentModel.objects.create(
            firstname = firstname,
            lastname = lastname,
            department = department
        )

        return redirect('student')

    return render(request, 'student/addstudent.html', {'departments': departments})



def add_department_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        DepartmentModel.objects.create(
                name = name,
            )
        return redirect('department')
    return render(request, 'department/adddepartment.html')



def view_department_page(request):
    departments = DepartmentModel.objects.all()
    return render(request, 'department/department.html', {'departments' : departments})
