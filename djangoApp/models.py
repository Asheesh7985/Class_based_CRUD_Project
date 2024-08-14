from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=70)
    edesg = models.CharField(max_length=70)
    esal = models.IntegerField()
