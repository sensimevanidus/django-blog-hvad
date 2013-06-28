# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from hvad.models import TranslatableModel, TranslatedFields


class BlogPost(TranslatableModel):
    """
    Represents a blog post.

    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'), related_name='blog_posts',)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True,)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True,)
    is_published = models.BooleanField(_('is published?'), default=False,)

    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=127,),
        slug=models.SlugField(_('slug'), unique=True,),
        excerpt=models.TextField(_('excerpt'), blank=True, null=True,),
        content=models.TextField(_('content'),),
    )

    def __unicode__(self):
        return u'%s' % self.title