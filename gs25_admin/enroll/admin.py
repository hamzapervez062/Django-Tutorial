from django.contrib import admin
from enroll.models import Student # Import the Student model from the models.py file in the same directory


#Alternative way to register the model with the admin site is by using the decorator

# @admin.register(Student) 
#create class 
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'password']  
    search_fields = ['name', 'email']   
    list_filter = ['name']  
    list_per_page = 10 


admin.site.register(Student, StudentAdmin)  # Register the Student model with the admin site using the StudentAdmin class   