from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect

import datetime
import  pytz

class IndexView(ListView):
    template_name = 'insta/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
         now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
        return Post.objects.filter(published_date__lte = datetime.datetime.now()).order_by('published_date')[:5]

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