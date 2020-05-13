from django import forms
from .models import Post, Comment, comment_to_comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'photo')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class comment_to_comment_form(forms.ModelForm):
    class Meta:
        model = comment_to_comment
        fields = ('text',)