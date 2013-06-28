# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import BlogPost

def posts(request):
    posts = BlogPost.objects.all()
    return render_to_response('blog_hvad/list.html', {'posts': posts}, context_instance=RequestContext(request))