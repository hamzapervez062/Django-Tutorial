from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='mypage')
    page_name = models.CharField(max_length=50)
    page_cat = models.CharField( max_length=50)
#related_name='mypage': This is the name of the reverse relation from User to Page. It will be available on the related objects.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=50)
    post_cat = models.CharField( max_length=50)

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=50)
    song_cat = models.CharField( max_length=50)
