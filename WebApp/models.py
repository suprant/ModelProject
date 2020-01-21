from django.db import models

# Create your models here.

class Emp(models.Model):
    EmpID=models.IntegerField()
    EmpName=models.CharField(max_length=30)
    EmpSal=models.FloatField()
    EmpAddr=models.CharField(max_length=30)
