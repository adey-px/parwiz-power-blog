from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Article


# Dynamic slug with signals, first indicate reciever
@receiver(pre_save, sender=Article)
def add_slug(instance, *args, **kwargs):
    """
    Get slug in url on click article title.
    Slug is included in models and passed
    in article_detail url. Article title is
    displayed in slug.
    """
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug
