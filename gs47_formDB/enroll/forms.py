from django import forms    
from django.core.exceptions import ValidationError  
from django.core import validators  

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()  
    password = forms.CharField(widget=forms.PasswordInput, )  
    repassword = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput )
