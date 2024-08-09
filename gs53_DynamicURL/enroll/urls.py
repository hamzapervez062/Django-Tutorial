from django.urls import path    
from enroll import views
from . import views 

urlpatterns = [
    # path('', views.home),
    path('reg/<my_id>', views.showformdata , name='add'), 
    path('form3/<idz>', views.Formdata, name='Formdata'),
]