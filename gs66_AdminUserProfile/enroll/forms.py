import re
from django.contrib.auth.models import User # This is the default User model that Django provides
from django.contrib.auth.forms import UserCreationForm # This is the default UserCreationForm that Django provides 
from django import forms   
from django.core import validators 
from django.contrib.auth.forms import AuthenticationForm  , PasswordChangeForm, UserChangeForm	

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(4)] ,required=True,  error_messages={'required':'First name is required plz'})
    class Meta:
        model = User
        fields = ['username', 'first_name',  'last_name', 'email']
        labels = {'email': 'Email'} 
      
        widgets = {'email':forms.TextInput(attrs={'placeholder':'Enter email here'}), 
            
                   'last_name':forms.TextInput(attrs={'placeholder':'Enter last name here'}),
                   }
        
   
         
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'} 
        widgets = {'email':forms.TextInput(attrs={'placeholder':'Enter email here',}), 
                   'username':forms.TextInput(attrs={'readonly':True}),
                   'date_joined':forms.TextInput(attrs={'readonly':True}),
                   'last_login':forms.TextInput(attrs={'readonly':True}),
                   'first_name':forms.TextInput(attrs={'placeholder':'Enter first name here'}),
                   'last_name':forms.TextInput(attrs={'placeholder':'Enter last name here'}),
                   }

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'} 
        widgets = {'email':forms.TextInput(attrs={'placeholder':'Enter email here'}), 
                   'username':forms.TextInput(attrs={'readonly':True}),
                   'date_joined':forms.TextInput(attrs={'readonly':True, 'readonly':True}),	
                   'last_login':forms.TextInput(attrs={'readonly':True}),
                   'first_name':forms.TextInput(attrs={'placeholder':'Enter first name here'}),
                   'last_name':forms.TextInput(attrs={'placeholder':'Enter last name here'}),
                   }
