"""
URL configuration for gs117_RedirectView project.

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
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.RedirectView.as_view(url='/about/'), name='indexs'),
    path('home/', views.RedirectView.as_view(pattern_name='indexs')),
    #pattern_name='indexs' is used to redirect to the URL with the name 'indexs'.
    path('home2/<int:pk>', views.SchoolView.as_view()),
    path('roll/<int:pk>/', views.TemplateView.as_view(template_name='school/index.html'), name='ml'),

    #
    path('home3/<int:pk>', views.SView.as_view()),

]
