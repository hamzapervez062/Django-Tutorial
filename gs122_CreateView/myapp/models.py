from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100) 
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detailed", kwargs={"pk": self.pk})
    # it is used to redirect the user to the detail page after the successful submission of the form.
    