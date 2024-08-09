from django.shortcuts import render
from .forms import StudentRegistration  
from django.http import HttpResponseRedirect    
# Create your views here.

def Formdata(request):  
    return render(request, 'enroll/userregistration.html')  

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']  
            email = fm.cleaned_data['email']    
            password = fm.cleaned_data['password'] 
            repassword = fm.cleaned_data['repassword'] 

            print('Form Validated', fm.cleaned_data)
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])

            #this method render data to another page witout changing url
            # return render(request, 'enroll/form2.html', {'name':name, 'email':email, 'password':password})

            #this method render data to another page with changing url
            return HttpResponseRedirect('/enroll/form3/')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
