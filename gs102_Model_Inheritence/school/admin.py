from django.contrib import admin
from .models import Student, Teacher, Contractor
from .models import ExamCenter, StudentExamCenter, MyExamCenter

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date', 'fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date', 'salary']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date', 'payment']

# Register your models here.    
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname', 'city']

@admin.register(StudentExamCenter)
class StudentExamCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'roll']


# Register your models here.
@admin.register(MyExamCenter)   
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname', 'city']

