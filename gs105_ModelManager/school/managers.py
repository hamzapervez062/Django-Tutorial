from django.db import models    

# Create custom manager	

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')  


#add  extra method in manager, it is used when we have to use same query agian and again.
class CustoomManager(models.Manager):
    def get_stu_roll_range(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2))
