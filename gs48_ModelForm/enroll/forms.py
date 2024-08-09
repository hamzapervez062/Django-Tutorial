from django import forms    
from .models import User 
from django.core import validators
from django.core.exceptions import ValidationError  


class StudentRegistration(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['name', 'email', 'password', 'repassword'] 
        labels = {'name':'Enter Names', 'email':'Enter Email', 'password':'Enter Password', 'repassword':'Re-Enter Password'}
        widgets = {'password':forms.PasswordInput, 'repassword':forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name here'}),}    
        help_texts = {'name':'Enter your full Name'} 
           
        error_messages = {'name':{'required':'Name is required plz'},	
                            'password':{'required':'Password is requiredz'},	
                          }   
        