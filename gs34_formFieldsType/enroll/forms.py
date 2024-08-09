from django import forms    

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your Name', # label is used to display the label of the field
                           label_suffix='-', # label_suffix is used to display the suffix of the label
                            initial='Ali', # initial is used to set the default value of the field
                            required=False, # required is used to make the field optional
                            disabled=True, # disabled is used to make the field disable
                            help_text='limit 30 characters', # help_text is used to display the help text of the field
                           widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name', 'class': 'form-control'})) # widget is used to set the HTML attribute of the field
    
    email = forms.EmailField() 
    
    password = forms.CharField(widget=forms.PasswordInput)  # PasswordInput widget is used to hide the password field