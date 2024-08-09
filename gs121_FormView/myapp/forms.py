from django import forms
from .models import School

class MyForm(forms.ModelForm):  
    class Meta:
        model = School
        fields = ['name', 'email', 'message']
        labels = {'name':'Name', 'email':'Email', 'message':'Message'}