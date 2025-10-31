from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StudentModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.firstname} {self.lastname}"