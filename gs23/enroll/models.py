from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
      
