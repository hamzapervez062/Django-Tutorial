from django.db import models
from django.core.exceptions import ValidationError  
from django.core import validators  

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70, validators=[validators.MinLengthValidator(4)])
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    repassword = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name    