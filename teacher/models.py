from django.db import models
from myapp.models import DepartmentModel

# Create your models here.
class TeacherInfo(models.Model):

	GENDER_CHOICES = [
		('Male', 'Male'),
		('Female', 'Female'),
		('Others', 'Others'),
	]

	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)


	def __str__ (self):
		return f"{self.firstname} {self.lastname}"
