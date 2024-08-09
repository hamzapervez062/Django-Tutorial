from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name