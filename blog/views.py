from django.views import generic
from .models import Post
from django.shortcuts import render

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order-by("-created_on")
    template_name = "index.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
