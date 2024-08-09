from django.db import models

# Abstract Base Classes

# An abstract base class is a class that is defined for the purpose of inheritance by subclasses, 
# but which is not itself intended to be instantiated. ]
# Abstract base classes are useful when you want to put some common information into a number of other models.
#  You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table. 
# Instead, when it is used as a base class for other models, its fields will be added to those of the child class.
class Commoninfo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    class Meta:
        abstract = True


class Student(Commoninfo):
    fees = models.IntegerField()

class Teacher(Commoninfo):
    salary = models.IntegerField()


class Contractor(Commoninfo):
    date = models.DateTimeField()
    payment = models.IntegerField()


# Multi-table Inheritance:
#auto one to one relationship
# Multi-table Inheritance and it is the default form of inheritance in Django. It is a type of inheritance in which every model has its own database table. The parent model is an abstract model and it does not have its own database table. The child model has a database table and a OneToOneField is created in the child model to associate it with the parent model. The child model has all the fields of the parent model and it can have its own fields.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
class StudentExamCenter(ExamCenter):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()


#Proxy Model:
# Proxy model is a type of model in which you can create a new model with the same fields and methods of an existing model. It is useful when you want to change the behavior of an existing model without changing the original model. You can create a proxy model by setting the Meta class of the model and setting proxy=True in the Meta class. The proxy model will have the same database table as the original model.
# When to use them?
# when you need to fit your models around an existing database, but they’re useful in new projects too.
class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['id']   # change the ordering of the model


    def __str__(self):
        return self.cname


