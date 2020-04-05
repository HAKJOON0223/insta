from django import forms
from .models import Post, Comment, comment_to_comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author', 'text', 'photo', 'published_date',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

class comment_to_comment_form(forms.ModelForm):
    class Meta:
        model = comment_to_comment
        fields = ('author', 'text')