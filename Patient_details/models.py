from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_name=models.CharField(max_length=30)
    patient_age=models.IntegerField()
    patient_problem=models.CharField(max_length=150)
    time=models.DateField("date registered")