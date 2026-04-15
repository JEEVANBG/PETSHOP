
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

def home(request):
    return HttpResponse("<h1>Hello Team, will start with Django soon</h1>")
