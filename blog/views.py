from django.shortcuts import render
from .models import Post2
# def list(request):
#     Data = {'Posts': Post.object.all().order_by("-date")}
#     return render(request, 'blog/blog.html', Data)
def list(request):
    Data = {"Posts": Post2.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)
def post(request, id):
    post = Post2.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})
