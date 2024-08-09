from django.contrib import admin
from enroll.models import blog
# Register your models here.
admin.site.register(blog)   
class blogAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']    
