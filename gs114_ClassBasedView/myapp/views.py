from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View   
from .forms import StudentRegistration


# Create your views here.

#Function based view    
def myview(request):
    # return HttpResponse("Hello, This is my first view") 
    context = {
        'name': 'Saira',
        'age': 23
    }
    return render(request, 'myapp/index.html', context)

#Class based view   
class MyView(View):
    def get(self, request):
        template_name = 'myapp/index.html'
        context = {
            'name': 'Sachin',
            'age': 24
        }
        return render(request, template_name, context)  

#    
class childmyview(MyView):
    name = "ALi"
    def get(self, request):
        # return HttpResponse("Hello, This is my child class based view")
        return HttpResponse(self.name)
    
####################################Forms##############################################
#function based view    
def student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            print('Form Validated')
            print('Name:', form.cleaned_data['name'])
            return HttpResponse("Submitted")
    else:
        form = StudentRegistration()
    return render(request, 'myapp/student.html', {'form': form})

#class based view
class stuclassview(View):
    def get(self, request):
        form = StudentRegistration()
        return render(request, 'myapp/student.html', {'form': form})
    def post(self, request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            print('Form Validated')
            print('Name:', form.cleaned_data['name'])
            return HttpResponse("Submitted")
        


#############################################################333

#Function based view    
def funview(request, template_name):
    template_name = template_name
    context = {"context": "Hellow"}
    return render(request, template_name ,context)

#class based 
class funclassview(MyView):
    template_name = ''
    def get(self, request):
       context = {"context": "Hellow"}
       return render(request, self.template_name ,context)



    

