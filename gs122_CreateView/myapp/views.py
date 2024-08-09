from django.shortcuts import render
from django.views.generic.edit import CreateView   
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from myapp.models import Books  
from django import forms

# Create your views here.
#CreateView: It is used to create a new record in the database.

class BooksCreateView(CreateView):
    model = Books
    fields = ['name', 'author'] 
    template_name = 'myapp/index.html'
    context_object_name = 'books'
    # success_url = '/thanks/'

    #to add class to the form fields
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget.attrs.update({'class': 'myclass'})
        form.fields['author'].widget = forms.TextInput(attrs={'class': 'myclass2'})
        return form

#it will create a form with fields name and author. and save the data in the database.
#template_name: It is used to specify the template file.
#context_object_name: It is used to specify the context variable name.
#success_url: It is used to specify the URL where the user will be redirected after the successful submission of the form.

class ThanksView(TemplateView):
    template_name = 'myapp/thank.html'

#TemplateView: It is used to render a template file.

class BooksDetailView(DetailView):
    model = Books
    template_name = 'myapp/detail.html'
    context_object_name = 'booksdetail'

    # def get_object(self):
    #     id_ = self.kwargs.get("pk")
    #     return Books.objects.get(id=id_)