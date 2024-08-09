from django.urls import path    
from . import views    

urlpatterns = [
    path('stu/', views.studentinfo),   # Call studentinfo function from views.py
]