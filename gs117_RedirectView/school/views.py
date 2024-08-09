from typing import Any
from django.shortcuts import render
from django.views.generic.base import RedirectView, TemplateView
#RedirectView: This view redirects to a specific URL. It is a class-based view that is used to redirect to a specific URL.	

class SchoolView(RedirectView):
    # url = '/'
    # url: This is the URL to which the view will redirect.	

    pattern_name = 'ml'
    # pattern_name: This is the name of the URL pattern to which the view will redirect.

    permanent = True
    # permanent: This is a boolean value that specifies whether the redirection is permanent or temporary. The default value is False, which means that the redirection is temporary.	

    query_string = True
    # query_string: This is a boolean value that specifies whether the query string is preserved in the redirection. The default value is False, which means that the query string is not preserved.
    #http://127.0.0.1:8000/roll/78/?jbbk True
    #http://127.0.0.1:8000/roll/78/ False

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        
        return super().get_redirect_url(*args, **kwargs)
    
class SView(TemplateView):
    template_name = 'school/index.html'
    query_string = True
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
    
        return context	
