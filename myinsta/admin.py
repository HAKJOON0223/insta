from django.contrib import admin
from .models import Post, Comment

class comment_inline(admin.TabularInline):
    model = Comment
    extra = 1

class post_admin(admin.ModelAdmin):
    inlines = [comment_inline]
    list_filter = ['published_date']


admin.site.register(Post, post_admin)

