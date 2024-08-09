from django.shortcuts import render
from enroll.models import Student   # Import Student class from models.py
# Create your views here.
def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'enroll/students.html', {'stud': stud})   # Pass students data to template