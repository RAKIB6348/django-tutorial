from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def homepage(request):
    return render(request, 'master.html')


def student_page(request):
    students = StudentModel.objects.all()
    return render(request, 'student.html', {'students' : students})


def add_student_page(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        department = request.POST.get('department')

        StudentModel.objects.create(
            firstname = firstname,
            lastname = lastname,
            department = department
        )

        return redirect('student')

    return render(request, 'addstudent.html')
