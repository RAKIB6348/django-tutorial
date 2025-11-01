from django.urls import path
from teacher.views import *

urlpatterns = [
	path('add/', teacher_add, name='teacheradd'),
	path('list/', teacher_list, name='teacherlist'),
]