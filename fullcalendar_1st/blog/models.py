from django.db import models

# Wagtail API
from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField

from wagtail.api import APIField

class BlogPageAuthor(Orderable):
    page = models.ForeignKey('blog.BlogPage', on_delete=models.CASCADE, related_name='authors')
    name = models.CharField(max_length=255)

    api_fields = [
        APIField('name'),
    ]

class BlogPage(Page):
    published_date = models.DateTimeField()
    body = RichTextField()
    private_field = models.CharField(max_length=255)

    # Export fields over the API
    api_fields = [
        APIField('published_date'),
        APIField('body'),
        APIField('authors'),  # This will nest the relevant BlogPageAuthor objects in the API response
    ]
#~