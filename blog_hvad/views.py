# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import BlogPost, BlogCategory

def posts(request):
    posts = BlogPost.objects.language().all()
    return render_to_response('blog_hvad/posts.html', {'posts': posts}, context_instance=RequestContext(request))

def category_posts(request, category_slug):
    try:
        category = BlogCategory.objects.language().get(slug__exact=category_slug)
        posts = category.blog_posts.all()
        return render_to_response('blog_hvad/category_posts.html', {'category': category, 'posts': posts}, context_instance=RequestContext(request))
    except BlogCategory.DoesNotExist:
        raise Http404

def post(request, slug):
    try:
        post = BlogPost.objects.language().get(slug=slug,)
    except BlogPost.DoesNotExist:
        raise Http404
    return render_to_response('blog_hvad/post.html', {'post': post}, context_instance=RequestContext(request))
