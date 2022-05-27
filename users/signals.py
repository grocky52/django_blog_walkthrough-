from . models import profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = User)
def Createprofile(sender, created, instance,  **kwargs):
    if created:
        profile.objects.create(user=instance)



def saveprofile(sender, instance, **kwargs):
    instance.profile.save()