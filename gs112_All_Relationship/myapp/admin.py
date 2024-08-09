from django.contrib import admin
from .models import Page, Post , Song
# Register your models here.
@admin.register(Page)   
class PageAdmin(admin.ModelAdmin):  
     list_display = ['user', 'page_name', 'page_cat'] 

@admin.register(Post)   
class PostAdmin(admin.ModelAdmin):  
     list_display = ['user', 'post_name', 'post_cat']

@admin.register(Song)   
class SongAdmin(admin.ModelAdmin):  
     list_display = ['song_name', 'song_cat']   
