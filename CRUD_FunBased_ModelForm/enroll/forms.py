from django import forms    
from enroll.models import User  
from django.core import validators  

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__' # This will display all fields of the model 
        # exclude = ['name'] # This will exclude the name field from the form	
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}
        widgets = {'password':forms.PasswordInput(attrs={'class':'form-control'}),
                    'name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'})}