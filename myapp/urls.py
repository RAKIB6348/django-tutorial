from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('student/', student_page, name='student'),
    path('add/student/', add_student_page, name='addstudent'),
    path('add/department/', add_department_page, name='add_department'),
    path('view/department/', view_department_page, name='department'),
]
