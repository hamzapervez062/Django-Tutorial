from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse    
from django.contrib.auth.models import User
from .models import Page, Post , Song
# Create your views here.
def home (request):
    data1 = User.objects.all()  
    data2 = User.objects.filter(email = 'hamza@uog.com')
    # data3 = User.objects.filter(page__page_cat='Music')
    data3 = User.objects.filter(mypage__page_cat='Music') # related_name='mypage' in Page model, it is the name of the reverse relation from User to Page	
    data4 = User.objects.filter(post__post_cat='Science')    
    data5 = User.objects.filter(song__song_cat='Pop')   
    return render(request, 'myapp/home.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})

def show_page(request):
    data = Page.objects.filter(page_cat='Music')

    return render(request, 'myapp/page.html', {'data': data})