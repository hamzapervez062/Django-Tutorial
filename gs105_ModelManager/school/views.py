from django.shortcuts import render
from django.http import HttpResponse    
from .models import School  

# Create your views here.
def home(request):
    # school_data = School.students.all()	  
    school_data = School.students.get_stu_roll_range(101, 105)
    return render(request,'school/home.html', {'schools':school_data})