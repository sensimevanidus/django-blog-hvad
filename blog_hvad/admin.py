from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import BlogPost

class BlogPostAdmin(TranslatableAdmin):
    class Meta:
        model = BlogPost

admin.site.register(BlogPost, BlogPostAdmin)