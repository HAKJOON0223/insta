from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    template_name = 'insta/index.html'
    model = Post