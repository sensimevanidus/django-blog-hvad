from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import BlogCategory, BlogPost

class BlogCategoryAdmin(TranslatableAdmin):
    class Meta:
        model = BlogCategory

    #
    # Workaround for prepopulated_fields and fieldsets from here:
    # https://github.com/KristianOellegaard/django-hvad/issues/10#issuecomment-5572524
    #
    def __init__(self, *args, **kwargs):
        super(BlogCategoryAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('name',)}

class BlogPostAdmin(TranslatableAdmin):
    class Meta:
        model = BlogPost

    #
    # Workaround for prepopulated_fields and fieldsets from here:
    # https://github.com/KristianOellegaard/django-hvad/issues/10#issuecomment-5572524
    #
    def __init__(self, *args, **kwargs):
        super(BlogPostAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)