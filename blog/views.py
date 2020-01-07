from django.shortcuts import render, get_object_or_404
from .models import Blog

# called by urls.py
def allblogs(request):
	blogs = Blog.objects
	return render(request, 'blog/allblogs.html', {'blogs':blogs}) # blog/ because it's in the blog directory

# in urls.py we specified an alias we named blog_id for the path /blog/<int>
def detail(request, blog_id):
	detailblog = get_object_or_404(Blog, pk=blog_id) #pk = primary key
	return render(request, 'blog/detail.html', {'blog':detailblog})