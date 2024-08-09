from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def tex(request):
    data = {
        'tax': 200
    }
    return render(request, 'fees/fees.html', data)
