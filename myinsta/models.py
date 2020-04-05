from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill, Transpose


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = ProcessedImageField(
            upload_to = 'photo/',
            processors = [Transpose(), ResizeToFill(980,980)],
            format = 'JPEG',
            options = {'quality': 80}
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default=False)


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
 

    def apporoved(self):
        self.apporoved_commnet = True
        self.save()
    
    def __str__(self):
        return self.text