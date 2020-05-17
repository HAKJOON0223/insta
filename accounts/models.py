from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill, Transpose
from PIL import Image #Pillow
from pilkit.processors import Thumbnail

def user_directory_path(instance, filename): 
	return '{0}/{1}'.format(instance.user.id, instance.user.id) 

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    profile_photo = ProcessedImageField(
            upload_to = user_directory_path,
            processors = [Transpose(), ResizeToFill(500,500)],
            format = 'JPEG',
            options = {'quality': 80},
            blank = True
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()