from django.contrib import admin
from myapp.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'department']
    search_fields = ['firstname', 'lastname', 'department']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']    

admin.site.register(StudentModel, StudentAdmin)
admin.site.register(DepartmentModel, DepartmentAdmin)
