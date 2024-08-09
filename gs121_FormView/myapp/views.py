from django.shortcuts import render
from .models import School
# Create your views here.
# FormView: FormView is a view that displays a form, processes submitted data, and renders a template with context.
#formmixin: A mixin class providing the ability to render a form and create and display form.
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from .forms import MyForm

class MyFormView(FormView):
    form_class = MyForm
    template_name = 'myapp/form.html'
    success_url = '/thanks/'
    context_object_name = 'form'

    def form_valid(self, form): 
        form.save()
        self.request.session['submitted_form_data'] = form.cleaned_data # Save the form data in the session
        return super().form_valid(form)

class ThanksTemplateView(ListView):
    template_name = 'myapp/thanks.html'
    model = School

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submitted_form_data'] =  self.request.session.get('submitted_form_data', {}) # Get the form data from the session
        context['fresh'] = School.objects.all()
        return context


#FormView: A view that displays a form, processes submitted data, and renders a template with context.
# RedirectView: A view that provides a redirect on any GET request.
#TemplateView: A view that renders a template.
#View: The most basic view, which does nothing at all. It's a blank page.