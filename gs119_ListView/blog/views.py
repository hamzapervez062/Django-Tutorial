from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student
# Create your views here.

#ListView: It is used to display the list of objects. It is a generic view provided by Django.
class StudentListView(ListView):
    model = Student
    # stud = Student.objects.all()
    # context = {
    #     'stud': stud
    # }
    # return render(request, 'blog/index.html', context)

    ########################################
    # template_name_suffix = '_get' #This is used to change the default template name suffix from '_list' to '_get.html
    ordering = ['name'] #This is used to sort the list of objects based on the name field.
    # paginate_by = 2 #This is used to display 2 objects per page.


    ############## Customize template name ##########################

    template_name = 'blog/index.html' #This is used to change the default template name from 'student_list.html' to 'index.html'
  
    ############## Customize Object name ##########################

    context_object_name = 'stud' #This is used to change the default object name from 'object_list' to 'stud'

    ##################  Filter querset ##############################
    #onlt get the students from Gujrat
    def get_queryset(self):
        return Student.objects.filter(city='Gujrat')
    
    #it is used to pass the additional context to the template
    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['fresh'] = Student.objects.all().order_by('name')
        return context
    
    ########################dynamic template rendering#########################

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'admin':
    #        template_name = 'blog/index.html'
    #     else:
    #         template_name = self.template_name
    #         return [template_name]

    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name = 'blog/superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'blog/staff.html'
    #     return [template_name]
    
    
    
