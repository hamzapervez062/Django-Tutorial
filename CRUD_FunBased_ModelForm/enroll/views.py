from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect  
from django.shortcuts import get_object_or_404
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST) 
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()   
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})
 

# def update_data(request, idz):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         po = User.objects.all().values_list('id', flat=True)
#         for i in po:
#             if i == idz:
#                 if fm.is_valid():
#                     nm = fm.cleaned_data['name']
#                     em = fm.cleaned_data['email']
#                     pw = fm.cleaned_data['password']
#                     reg = User(id=idz, name=nm, email=em, password=pw)
#                     reg.save()         
#         # return HttpResponseRedirect('/update/'+str(idz)+'/')
#     else:
#         fm = StudentRegistration()
#     stud = User.objects.filter(id = idz).values()  
#     return render(request, 'enroll/updatestudent.html', {'data':stud, 'form':fm})	
	
def get_user(id):
  user = User.objects.get(pk=id)
  return [user]

def update_data(request, idz):
    if request.method == 'POST':
        pi = User.objects.get(pk=idz)
        fm = StudentRegistration(request.POST, instance=pi)
        print("pi",pi) 
        print("fm1",fm)   
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=idz)  
        fm = StudentRegistration(instance=pi)
    # stud = User.objects.filter(id = idz).values() 
    stud = get_user(idz)
    return render(request, 'enroll/updatestudent.html', {'form':fm, 'data':stud})


def delete_data(request, idz):
    # de = get_object_or_404(User, pk=idz)
    pi = User.objects.get(pk=idz)
    # print("de",de)
    print("pi",pi)    
    pi.delete()
    return HttpResponseRedirect('/')      