from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


from .models import Post
class PostListView(ListView):
    model = Post
    
    template_name = "core/main.html"
    
class PostDetailView(DetailView):
    model = Post
    
    template_name = "core/detail.html"
        



