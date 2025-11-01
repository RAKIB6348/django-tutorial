from django.shortcuts import render
from teacher.models import *

# Create your views here.
def teacher_add(request):
	teachers = TeacherInfo.objects.all()

	if request.method == 'POST':
		


	return render(request, 'teacher/addteacher.html')



def teacher_list(request):
	teachers = TeacherInfo.objects.all()
	return render(request, 'teacher/teacherlist.html', {'teachers': teachers})