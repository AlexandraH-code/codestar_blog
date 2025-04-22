from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post


# Create your views here.
# def my_blog(request):
    # return HttpResponse("Hello, Blog!")
class PostList(generic.ListView):
    # model = Post
    # queryset = Post.objects.all()
    # queryset = Post.objects.filter(author=1)
    # queryset = Post.objects.all().order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6
    queryset = Post.objects.filter(status=1)
    