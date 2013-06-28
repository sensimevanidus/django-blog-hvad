# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import BlogPost

def posts(request):
    posts = BlogPost.objects.all()
    return render_to_response('blog_hvad/list.html', {'posts': posts}, context_instance=RequestContext(request))

def post(request, slug):
    try:
        post = BlogPost.objects.language().get(slug=slug,)
    except BlogPost.DoesNotExist:
        raise Http404
    return render_to_response('blog_hvad/post.html', {'post': post}, context_instance=RequestContext(request))