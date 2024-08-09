from django.shortcuts import render
from django.views.generic.edit import CreateView , DeleteView
from django.views.generic import TemplateView
from myapp.models import Books  



class BooksCreateView(CreateView):
    model = Books
    fields = ['name', 'author'] 
    template_name = 'myapp/index.html'
    context_object_name = 'books'
    success_url = '/thanks/'

    #to add class to the form fields
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget.attrs.update({'class': 'myclass'})
        # form.fields['author'].widget = forms.TextInput(attrs={'class': 'myclass2'})
        return form

class ThanksView(TemplateView):
    template_name = 'myapp/thank.html'

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/create/'
    template_name = 'myapp/confim_delete.html'
