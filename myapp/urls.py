from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('student/', student_page, name='student'),
    path('add/student/', add_student_page, name='addstudent'),
]
