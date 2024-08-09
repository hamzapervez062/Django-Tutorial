from django import forms 
from django.core.exceptions import ValidationError  
from django.core import validators  

#custom validation
def starts_with_a(value):
    if value[0].lower() != 'a':
        raise ValidationError('Name should start with a')
    
#built-in validation
class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(4)], error_messages={'required':'Enter Name'})
    email = forms.EmailField(validators=[starts_with_a], error_messages={'required':'Enter Email'} , max_length=40, min_length=25)  
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Password'})  
    repassword = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput, error_messages={'required':'Re-Enter Password'} )


#cleaning and validating specific field 
    # def clean_name(self):
    #     inputname = self.cleaned_data['name']
    #     #check if name is less than 4 characters
    #     if len(inputname) < 4:
    #         raise forms.ValidationError('The minimum length of name should be 4')   
    #     return inputname  

#cleaning and validating all fields 
    # def clean(self):
    #     cleaned_data = super().clean()
    #     inputname = cleaned_data['name']
    #     inputemail = cleaned_data['email']
    #     inputpassword = cleaned_data['password']
    #     #check if name is less than 4 characters
    #     if len(inputname) < 4:
    #         raise forms.ValidationError('The minimum length of name should be 4')   
    #     #check if password is less than 6 characters
    #     if len(inputemail) < 6:
    #         raise forms.ValidationError('The minimum length of password should be 6')   
    #     #check if password is less than 6 characters
    #     if len(inputpassword) < 6:
    #         raise forms.ValidationError('The minimum length of password should be 6')   
    #     return cleaned_data  

#matching password and repassword   
    # def clean(self):
    #     cleaned_data = super().clean()
    #     inputpassword = cleaned_data['password']
    #     inputrepassword = cleaned_data['repassword']
    #     #check if password is less than 6 characters
    #     if inputpassword != inputrepassword:
    #         raise forms.ValidationError('Password and Re-Password does not match')   
    #     return cleaned_data
            
       