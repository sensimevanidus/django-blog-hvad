from django.conf.urls import *
from django.utils.translation import ugettext_lazy as _

urlpatterns = patterns('blog_hvad.views',
    url(_(r'^posts/?$'), 'posts', name='posts'),
)