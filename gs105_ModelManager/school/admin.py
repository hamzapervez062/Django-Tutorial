from django.contrib import admin
from .models import School  
# Register your models here.
@admin.register(School)	
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name','roll'] 
    search_fields = ['name']    
    list_filter = ['name']  
