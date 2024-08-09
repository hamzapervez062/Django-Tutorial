from django.shortcuts import render
from .models import User    
from .forms import StudentRegistration  
from django.http import HttpResponseRedirect    

# Create your views here.
def home(request):  
    
    pi = User.objects.all()
    po = User.objects.all().values_list('name', flat=True)
    get = User.objects.get(id=1)
    only_column = User.objects.values_list('name') # it will return only name  column
    only_row = User.objects.filter(id = 1).values() 
    
    print("only_row",only_row)
    print("only_column",po)

    return render(request, 'enroll/home.html', {'data':pi})


def Formdata(request, idz):     
    dic = {}
    po = User.objects.all().values_list('id', flat=True)
    for i in po:
        if i == int(idz):
            only_row = User.objects.filter(id = i).values() 
            dic = only_row 
    return render(request, 'enroll/form3.html', {'data':dic}) 

def showformdata(request, my_id):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)  
        if fm.is_valid():
            name = fm.cleaned_data['name']  
            email = fm.cleaned_data['email']    
            password = fm.cleaned_data['password'] 
            repassword = fm.cleaned_data['repassword'] 

            reg = User(name=name, email=email, password=password, repassword=repassword)    
            reg.save()
            
            return HttpResponseRedirect('/enroll/form3/'+str(reg.id))	
    else:
        fm = StudentRegistration()  
    return render(request, 'enroll/userregistration.html', {'form':fm}) 
