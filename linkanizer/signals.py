from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Link
from .tasks import scrape_link_metadata


@receiver(post_save, sender=Link)
def on_link_create(sender, instance: Link, created: bool, **kwargs: dict):
    if created:
        scrape_link_metadata.apply_async(args=(instance.id,))
