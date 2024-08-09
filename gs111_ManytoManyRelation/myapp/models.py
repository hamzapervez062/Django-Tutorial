from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    user = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
def written_by(self):
    return ', '.join([user.username for user in self.user.all()])