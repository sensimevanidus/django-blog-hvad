# -*- coding: utf-8 -*-
from django import template
from ..models import BlogCategory


register = template.Library()

@register.assignment_tag
def get_blog_categories(language):
    return BlogCategory.objects.language(language).all()