from django.shortcuts import render
from django.http import HttpRequest

from .models import Post

# Create your views here.

def post_list(request:HttpRequest):
    posts = Post.objects.all()
    print(posts)
    post1 = posts[0]
    print(post1.published_recently())
    return render(request,"blogapp/post_list.html", context={"list":posts})