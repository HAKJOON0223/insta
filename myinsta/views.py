from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post, Comment, comment_to_comment
from .forms import PostForm, CommentForm, comment_to_comment_form
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
import os


@login_required
def IndexView(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'myinsta/index.html',
    {'posts': posts}
    )
    
    
@login_required
def NewPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.user_id = request.user.id
            post.save()
            return redirect('IndexView')
    else:
        form = PostForm()
    return render(request, 'myinsta/EditPost.html', {'form': form})

@login_required
def EditPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.user_id = request.user.id
            post.save()
            return redirect('IndexView')
    else:
        form = PostForm(instance=post)
    return render(request, 'myinsta/EditPost.html', {'form': form})

@login_required
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
            comment.author = request.user
            comment.user_id = request.user.id
            comment.post = post
            comment.save()
            return redirect('add_comment_page', pk=post.pk)

    else:
        form = CommentForm()

    if request.method == "POST":
        form_comment_to_comment = comment_to_comment_form(request.POST)
        if form_comment_to_comment.is_valid():
            comment_to_comment = form_comment_to_comment.save(commit=False)
            comment_to_comment.author = request.user
            comment_to_comment.user_id = request.user.id
            comment_to_comment.comment = comment
            comment_to_comment.save()
            return redirect('add_comment_page', pk=post.pk)
    else:
        form = comment_to_comment_form()

    return render(request,
    'myinsta/add_comment_page.html',
    {'form_comment': form_comment,
    'form_comment_to_comment': form_comment_t_comment,
    'comment': comment,
    'comment_to_comment':comment_t_comment},
    )

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('IndexView')

