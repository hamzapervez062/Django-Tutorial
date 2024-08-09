from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration	    
from .models import User    
from django.http import HttpResponseRedirect
# Create your views here.

def student_form(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks', )
    else:
        form = StudentRegistration()
    return render(request, 'enroll/student.html', {'form':form})	

def teacher_form(request):
    if request.method == 'POST':
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()

            # pi = User.objects.all().values()   
            # query_string = f"?pi={pi}"
            # return HttpResponseRedirect(f'/thanks/{query_string}')
            
            return HttpResponseRedirect('/thanks', )
   
    else:
        form = TeacherRegistration()
    pi = User.objects.all().values()
    return render(request, 'enroll/teacher.html', {'form':form})   

def thanks(request):
    #get the data from the url  
    # pi = request.GET.get('pi')

    pi = User.objects.all().values('teacher_name')  
    return render(request, 'enroll/thanks.html', {'pi':pi}) 
