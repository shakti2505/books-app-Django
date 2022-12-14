from django.db.models.signals import post_save
from django.contrib.auth.models import User

#receiver to receive the signal to perform the action
from django.dispatch import receiver
from .models import Profile

# function to build profile

# when receiver receivs the signal post_save singnal from the sender the fuction build_profile will run and createa Profile of that user.
@receiver(post_save, sender = User)
def build_profile(sender, instance, created, **kwargs ):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()






