from django import forms    
from enroll.models import User  

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']    
        labels = {'name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}