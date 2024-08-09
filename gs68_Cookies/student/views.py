from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name', 'Girish', max_age=30)
    return response

def getcookie(request):
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'student/getcookie.html', {'name': name})   

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response 