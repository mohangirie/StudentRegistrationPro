from django.db import models

# Create your models here.


class StudentModel(models.Model):
    Roll_Number = models.IntegerField(primary_key=True)
    Student_Name = models.CharField(max_length=30)
    Mobile = models.BigIntegerField()
    Fee = models.IntegerField()
    Email = models.EmailField(max_length=50)
    DateOfBirth = models.DateField(max_length=100)
    Gender = models.CharField(max_length=20)
    Course = models.CharField(max_length=20)
    InstituteName = models.CharField(max_length=50)
    Address = models.TextField(max_length=50)
