from django.contrib import admin
from teacher.models import *

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
	list_display = ['firstname', 'lastname', 'gender', 'department']
	search_fields = ['firstname', 'lastname']


admin.site.register(TeacherInfo, TeacherAdmin)

