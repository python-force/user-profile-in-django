from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.core.models import Profile
from django.contrib.auth.models import User
import pdb

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        pdb.set_trace()
    instance.profile.save()