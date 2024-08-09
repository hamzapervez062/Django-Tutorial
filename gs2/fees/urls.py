
from django.urls import path
from . import views 

urlpatterns = [
    path('tex/', views.tex)
]
