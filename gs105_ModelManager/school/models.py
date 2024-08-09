from django.db import models
from .managers import CustomManager , CustoomManager
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()    

    #change model name in admin panel  , by default it is School object	 
    # students = models.Manager()  

    # students = CustomManager()  
    students = CustoomManager()

