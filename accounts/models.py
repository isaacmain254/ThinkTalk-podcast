from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=950, blank=True)
    profession = models.TextField(max_length=200, blank=True)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        signal to create 'Profile' Model automatically when User instance is created
        """
        if created:
            Profile.objects.create(user=instance)
