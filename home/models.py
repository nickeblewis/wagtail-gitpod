from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    banner_title = models.CharField(max_length=50, default='Hello World!')
    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]