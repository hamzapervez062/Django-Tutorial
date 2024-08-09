from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect  
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.
class UserAddShowView(TemplateView):
    template_name = 'myapp/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'form':fm, 'stu':stud}
        return context
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
        return HttpResponseRedirect('/')


def get_user(id):
  user = User.objects.get(pk=id)
  return [user]

# class UserUpdateData2(View):
#     def get(self, request, idz):
#         pi = User.objects.get(pk=idz)
#         fm = StudentRegistration(instance=pi)
#         stud = get_user(idz)
#         return render(request, 'myapp/updatestudent.html', {'form':fm, 'data':stud})
    
#     def post(self, request, idz):
#         pi = User.objects.get(pk=idz)
#         fm = StudentRegistration(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#         return HttpResponseRedirect('/')

class UserUpdateData(TemplateView):
    template_name = 'myapp/updatestudent.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idz = kwargs['idz']
        pi = User.objects.get(pk=idz)
        fm = StudentRegistration(instance=pi)
        stud = get_user(idz)
        context = {'form':fm, 'data':stud}
        return context
    
    def post(self, request, **kwargs):
        idz = kwargs['idz']
        print('idz', idz)
        pi = User.objects.get(pk=idz)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    

class UserDeleteData(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        print("kwargs",kwargs)
        idz = kwargs['idz']
        pi = User.objects.get(pk=idz)
        pi.delete()
        return super().get_redirect_url(*args, **kwargs)