from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100) 
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
