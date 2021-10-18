from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
            user = instance
            global profile 
            profile = Profile.objects.create(
            user = user,
            email = user.email,
        
            )
    subject = 'Welcome to Historic Stops!'
    message = 'We are glad you registered. Login to Historic Stops to get started.'

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [profile.email],
        fail_silently=False,
        )
    


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
