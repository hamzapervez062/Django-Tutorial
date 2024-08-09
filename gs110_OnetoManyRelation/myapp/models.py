from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)


class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #when main user is deleted, but its post is not deleted

    title = models.CharField(max_length=100)
    cat = models.TextField()

    def __str__(self):
        return self.title