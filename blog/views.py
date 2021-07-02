from django.shortcuts import render,get_object_or_404
from .models import BlogProject


def all_blogs(request):
    blog = BlogProject.objects.order_by('-date')
    return render(request,'blog/all_blogs.html', {'blog': blog})


def detail(request, blog_id):
    blog1 =get_object_or_404(BlogProject, pk=blog_id)
    return render(request,'blog/detail.html',{'blog1':blog1})
