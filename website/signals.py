from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, UserRole


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Assume que 2 é o ID para "Registradores"
        registrador_role = UserRole.objects.get(pk=2)
        UserProfile.objects.create(
            user=instance, role=registrador_role, email=instance.email)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
