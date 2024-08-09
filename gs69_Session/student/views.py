from django.shortcuts import render


def setsession(request):
    request.session['name'] = 'Girish'
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session.get('name', default = 'Guest')
    return render(request, 'student/getsession.html', {'name': name})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')