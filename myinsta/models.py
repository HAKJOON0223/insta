from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = ProcessedImageField(
            upload_to = 'photo/',
            processors = [Thumbnail(600,600)],
            format = 'JPEG',
            options = {'quality': 60}
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title