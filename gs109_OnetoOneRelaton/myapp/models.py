from django.db import models
from django.contrib.auth.models import User

#One To One REaltionship

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()

class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    page_name = models.CharField(max_length=50)
    page_cat = models.CharField(max_length=50)
    page_publish_date = models.DateField()

    def __str__(self):
        return self.page_name	
    
#on_delete=models.CASCADE: If the user is deleted, the page will also be deleted.
#on_delete=models.protect: If the user is deleted, the page will not be deleted.
#limit_choices_to = {'is_staff': True}: Only the staff members can be selected as a user for the page.

#--------------------------------------------------------------------------------
#one to one with model inheritance
class Like(Page):
    panna =  models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True,
                                   limit_choices_to={'is_staff': True}, parent_link=True)
    likes = models.IntegerField()


#parent_link=True: It is used to create a parent link in the database table and it is used to create a one-to-one relationship with the parent model.


