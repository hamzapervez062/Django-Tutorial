from django.shortcuts import render
from .models import User    
from .forms import StudentRegistration  
from django.http import HttpResponseRedirect 
   


# Create your views here.
def Formdata(request):  
    return render(request, 'enroll/form3.html')  

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']  
            email = fm.cleaned_data['email']    
            password = fm.cleaned_data['password'] 
            repassword = fm.cleaned_data['repassword'] 

            reg = User(name=name, email=email, password=password, repassword=repassword)    
            reg.save()
            
            return HttpResponseRedirect('/enroll/form3/')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
