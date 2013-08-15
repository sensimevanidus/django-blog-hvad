from django.conf.urls import *
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('blog_hvad.views',
    url(_(r'^posts/?$'), 'posts', name='posts'),
    url(_(r'^posts/(?P<category_slug>.+)/?$'), 'category_posts', name='category_posts'),
    url(_(r'^post/(?P<slug>.+)/?$'), 'post', name='post'),
)