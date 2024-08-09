from django.shortcuts import render
from django.http import HttpResponse  
from enroll.forms import StudentRegistration  
from enroll.models import User
from django.contrib import messages 


# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)  
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been created successfully')
            messages.error(request, 'Your account has not been created successfully')
            print(messages.get_level(request))
            messages.debug(request, 'Your account has been created successfully')   
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'Your account has been created succes]\sfully')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})

