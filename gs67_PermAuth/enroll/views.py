from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponseRedirect 
from django.contrib import messages   
from .forms import SignUpForm        
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group

# Create your views here.
#signup page
def sign_up(request):
    if request.method == 'POST':
        # fm = UserCreationForm(request.POST)
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username'] 
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username is already taken')
                return HttpResponseRedirect('/signup/')
            
            user = fm.save()
            
            group = Group.objects.get(name='Editor' ) # 'Editor' is the name of the group created in admin site 
            user.groups.add(group)
            messages.success(request, 'Account Created Successfully')

    else:
        # fm = UserCreationForm()
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})

#login page
def log_in(request):
    if not request.user.is_authenticated:	
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username'] 
                upass = fm.cleaned_data['password'] 
                user = authenticate(username=uname, password=upass) 

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')    
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
    
# profile page for user and admin
def user_dashbooard(request):
    if request.user.is_authenticated:

        return render(request, 'enroll/dashboard.html', {'name':request.user.username})

       
    else:
        return HttpResponseRedirect('/login/')
    
#logout
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')  

