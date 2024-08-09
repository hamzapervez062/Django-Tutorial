from django import forms    
from enroll.models import User  
from django.core import validators  

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 
        exclude = ['teacher_name']
        labels = {'student_name':'Enter Name', 'email':'Enter Email', 'password':'Enter Password'}
        widgets = {'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password here'}),
                    'student_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control',})}
        validators = {
            'student_name': [validators.MaxLengthValidator(10), validators.MinLengthValidator(4)]
        }
        error_messages = {'student_name':{'required':'Name is required plz'},	
                            'password':{'required':'Password is requiredz'},	
                          }   
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = '__all__'  
        exclude = ['student_name']
        labels = {'teacher_name':'Enter Teacher Name', 'email':'Enter Email', 'password':'Enter Password'}  
        