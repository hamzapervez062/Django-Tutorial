from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)   
class userAdmin(admin.ModelAdmin):  
    list_display = ['id', 'student_name', 'teacher_name', 'email', 'password']  
    list_filter = ['student_name', 'teacher_name']  
    search_fields = ['student_name', 'teacher_name']  
    ordering = ['id']  
    list_per_page = 10  
    
