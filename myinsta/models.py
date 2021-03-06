from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill, Transpose
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
import os

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True)
    text = models.TextField(blank=True)
    photo = ProcessedImageField(
            upload_to = 'myinsta/photo/',
            processors = [Transpose(), ResizeToFill(980,980)],
            format = 'JPEG',
            options = {'quality': 80},
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)
    user_id = models.TextField(blank=True)

    def __str__(self):
        return self.text

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(Post, self).delete(*args, **kargs)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comment', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True )
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default=False)
    user_id = models.TextField(blank=True)


    def approved(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class comment_to_comment(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='comment_to_comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    apporved_comment = models.BooleanField(default = False)
    user_id = models.TextField(blank=True)
 

    def apporoved(self):
        self.apporoved_commnet = True
        self.save()
    
    def __str__(self):
        return self.text