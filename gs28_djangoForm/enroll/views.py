from django.shortcuts import render
from enroll.forms import StudentRegistration    
# Create your views here.

def showformdata(request):  
    fm = StudentRegistration(auto_id="some_%s", #auto_id is used to set the id of the field
                             label_suffix="-", #label_suffix is used to remove the colon(:) from the label 
                             initial={'name': 'ali'}, #initial is used to set the default value of the field
                             field_order=['name', 'phone', 'email', 'address', 'password'], #field_order is used to set the order of the field   
                             )    
    return render(request, 'enroll/userregistration.html', {'form': fm})    