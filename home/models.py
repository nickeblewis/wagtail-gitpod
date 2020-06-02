from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)
    banner_title = models.CharField(max_length=50, default='Hello World!')

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel('body', classname='full')
    ]