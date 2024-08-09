from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    data = {
        'name': 'Python'
    }
    return render(request, 'course/course.html', data)