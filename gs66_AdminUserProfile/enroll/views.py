from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.http import HttpResponseRedirect 
from django.contrib import messages   
from .forms import SignUpForm        
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash

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
            
            fm.save()
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
                    return HttpResponseRedirect('/profile/')    
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    
# profile page for user and admin
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:   
                #Admin 
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()  
            else:
                #User
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None

            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile Updated Successfully')
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()  
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'form':fm, 'name':request.user.username, 'users':users})
    else:
        return HttpResponseRedirect('/login/')
    
def get_user(id):
  user = User.objects.get(pk=id)
  return [user]
    
#user detail page
def user_detail(request, id):
    pi =  get_user(id)
    if request.user.is_authenticated:
        return render(request, 'enroll/userdetails.html', {'data':pi})
    else:

        return HttpResponseRedirect('/login/')

#change password page   
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')    
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
#change password page2
def change_password2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')    
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# logout page
def user_logout(request):
    logout(request)
    return redirect('/login/')