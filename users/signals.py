"""We need some way to tell django to create a new profile object every time a user object is created. Remember the OneToOne relationship defined in models.py under users. But that only defines a relationship. While a profile linked to every created user can be accessed from the admin page, we need to tell django to do it automatically. Thats where signals comes in.

https://docs.djangoproject.com/en/2.1/topics/signals/

"""
from django.db.models.signals import post_save # post_save is a signal sent after an action is performed
from django.contrib.auth.models import User
from django.dispatch import receiver # Receiver is a fucntion that receives the signal i.e., the post_save signal. The receiver is the create_profile function
from .models import Profile

@receiver(post_save, sender = User) # When the sender (User) sends a post_save signal
def create_profile(sender, instance, created, **kwargs): # Invoke the create_profile function
    if created: # If the signal to create the profile was sent
        Profile.objects.create(user = instance) # Then create the profile


@receiver(post_save, sender = User) # When the sender (User) sends a post_save signal
def save_profile(sender, instance, **kwargs): # Invoke the save_profile function
    instance.profile.save()
