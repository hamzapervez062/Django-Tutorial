from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher, Contractor
# Create your views here.
def home(request):
    stu = Student.objects.all() 
    tea = Teacher.objects.all()
    con = Contractor.objects.all()
    return render(request, 'school/home.html', {'stu':stu, 'tea':tea, 'con':con})