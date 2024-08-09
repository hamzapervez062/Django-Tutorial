from django.contrib import admin
from myapp.models import Books  
# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']