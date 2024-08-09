from django import forms    
from django.core import validators  
from django.core.exceptions import ValidationError  

#fORM API method
# CLASS BASED VIEW
class StudentRegistration(forms.Form):
    name = forms.CharField()    
