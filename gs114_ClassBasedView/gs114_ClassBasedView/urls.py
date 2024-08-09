"""
URL configuration for gs114_ClassBasedView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import MyView, myview, childmyview, student, stuclassview
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myview/', view=myview, name='myview'),
    path('myclassview/', view=MyView.as_view(), name='myclassview'),
    path('childmyview/', view=childmyview.as_view(name='hamza'), name='childmyview'),
    #
    path('stu/', view=student),
    path('stud/', view=stuclassview.as_view(), name='stuclassview'),
    #
    path('fun1/', views.funview, {'template_name': 'myapp/fun1.html'},),
    path('fun2/', views.funview, {'template_name': 'myapp/fun2.html'}, ),

    path('funcls1/', views.funclassview.as_view(template_name = 'myapp/fun1.html')),
    path('funcls2/', views.funclassview.as_view(template_name = 'myapp/fun2.html')),
    
]
