from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, pre_init, post_init
from django.core.signals import request_started, request_finished   


# connect signal with receiver using decorator
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("User Logged In")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print("Kwargs: ", kwargs)
    print("User Details: ", User.objects.get(username=user))    

# connect signal with receiver  
# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("User Logged Out")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print("Kwargs: ", kwargs)
    print("User Details: ", User.objects.get(username=user))

@receiver(user_login_failed, sender=User)
def login_failed(sender, credentials, request, **kwargs):
    print("Login Failed")
    print("Sender: ", sender)
    print("Credentials: ", credentials)
    print("Request: ", request)
    print("Kwargs: ", kwargs)



#cache example
@receiver(pre_save, sender=User)
def pre_save_receiver(sender, instance, **kwargs):
    print("Pre Save Signal")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print("Kwargs: ", kwargs)

@receiver(post_save, sender=User)   
def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        print("User Created")
        print("Post Save Signal")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print("Kwargs: ", kwargs)
    else:
        print("User Updated")
        print("Post Save Signal")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print("Kwargs: ", kwargs)

@receiver(pre_delete, sender=User)
def pre_delete_receiver(sender, instance, **kwargs):
    print("Pre Delete Signal")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print("Kwargs: ", kwargs)

@receiver(post_delete, sender=User)
def post_delete_receiver(sender, instance, **kwargs):
    print("Post Delete Signal")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print("Kwargs: ", kwargs)

@receiver(pre_delete, sender=User)  
def pre_delete_receiver(sender, instance, **kwargs):
    print("Pre Delete Signal")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print("Kwargs: ", kwargs)


# when model is initialized from database 
@receiver(pre_init, sender=User)    
def pre_init_receiver(sender, *args, **kwargs):
    print("Pre Init Signal")
    print("Sender: ", sender)
    print("Args: ", args)
    print("Kwargs: ", kwargs)


# when 
@receiver(post_init, sender=User)
def post_init_receiver(sender, *args, **kwargs):
    print("Post Init Signal")
    print("Sender: ", sender)
    print("Args: ", args)
    print("Kwargs: ", kwargs)

# when request is started and finished  
@receiver(request_started)  
def request_started_receiver(sender, environ, **kwargs):
    print("Request Started")
    print("Sender: ", sender)
    print("Environ: ", environ)
    print("Kwargs: ", kwargs)