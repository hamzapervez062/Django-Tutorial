from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
#it renders a given template, with the context containing parameters captured from the URL.
# it inherits templateResponseMixin and contextMixin, view
#TemplateView : It is used to render a given template. It inherits TemplateResponseMixin and ContextMixin, view.
###############3

class SchoolView(TemplateView):
    template_name = 'school/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Django School'
        context['roll'] = 101
        print(context)
        print(kwargs)
        return context	
# **kwargs: It is used to pass a keyworded, variable-length argument list.