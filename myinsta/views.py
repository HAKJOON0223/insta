from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
from django.shortcuts import render

class IndexView(ListView):
    template_name = 'insta/index.html'
    model = Post

def EditPost(request):
    form = PostForm()
    return render(request, 'insta/EditPost.html', {'form': form})