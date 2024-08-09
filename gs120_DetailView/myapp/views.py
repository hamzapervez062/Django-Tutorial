from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book

# Create your views here.
# Use ListView to display lists/collections of multiple objects
# Use DetailView to display detailed information for a single object
# ListView is for listings, DetailView is for individual item details


class BookListView(ListView):
    model = Book
    template_name = 'myapp/books_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/detail.html'
    context_object_name = 'book'
    # pk_url_kwarg = 'id' #This is used to change the default primary key name from 'pk' to 'id' from the URL.  path('books/<int:pk>/',

    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['fresh'] = self.model.objects.all().order_by('title')
        return context

    
