
from django.db.models.signals import post_save  # importing post_save (built-in user model)
from django.contrib.auth.models import User
from django.dispatch import receiver    # its a decorator
from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
