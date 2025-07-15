from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Vinculo(models.Model):
    vinculo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.vinculo

class User(AbstractUser):
    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(blank=True, null=True)
    primeiro_nome = models.CharField(max_length=50, blank=True)
    ultimo_sobrenome = models.CharField(max_length=50, blank=True)

    def __str__(self):
            return self.user.email if self.user.email else self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img = Image.open(self.avatar.path)
            img = img.resize((350, 350), Image.LANCZOS)
            img.save(self.avatar.path)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()