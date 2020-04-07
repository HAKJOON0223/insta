from django.views.generic import ListView, DetailView
from .models import Post, Comment, comment_to_comment
from .forms import PostForm, CommentForm, comment_to_comment_form
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import os



def IndexView(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'insta/index.html', {'posts': posts})
    
def EditPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('IndexView')
    else:
        form = PostForm()
    return render(request, 'insta/EditPost.html', {'form': form})

def add_comment_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = post.comment.all
    comment_t_comment = Comment.objects.all()
    form_comment = CommentForm(request.POST)
    form_comment_t_comment = comment_to_comment_form(request.POST)
    if request.method == "POST":
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('add_comment_page', pk=post.pk)
    else:
        form = CommentForm()

    if request.method == "POST":
        form_comment_to_comment = comment_to_comment_form(request.POST)
        if form_comment_to_comment.is_valid():
            comment_to_comment = form_comment_to_comment.save(commit=False)
            comment_to_comment.comment = comment
            comment_to_comment.save()
            return redirect('add_comment_page', pk=post.pk)
    else:
        form = comment_to_comment_form()

    return render(request,
    'insta/add_comment_page.html',
    {'form_comment': form_comment,
    'form_comment_to_comment': form_comment_t_comment,
    'comment': comment,
    'comment_to_comment':comment_t_comment},
    )

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('IndexView')

