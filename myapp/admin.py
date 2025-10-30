from django.contrib import admin
from myapp.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'department']
    search_fields = ['firstname', 'lastname', 'department']

admin.site.register(StudentModel, StudentAdmin)
