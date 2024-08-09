from django.urls import path    

from . import views 

urlpatterns = [ 
    path('reg/', views.showformdata), 
    path('form3/', views.Formdata), 
]