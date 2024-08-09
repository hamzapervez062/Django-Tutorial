from django import forms    

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()
    key = forms.CharField(widget=forms.HiddenInput)  # HiddenInput widget is used to hide the field from the user
    password = forms.CharField(widget=forms.PasswordInput)  # PasswordInput widget is used to hide the password field
    # Compare this snippet from gs28_djangoForm/enroll/views.py:    