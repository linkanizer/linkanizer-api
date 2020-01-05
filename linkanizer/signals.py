from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Link, List
from .tasks import scrape_link_metadata


@receiver(post_save, sender=Link)
def on_link_create(sender, instance: Link, created: bool, **kwargs: dict):
    if created:
        scrape_link_metadata.apply_async(args=(instance.id,))


@receiver(post_delete, sender=Link)
def on_link_delete(sender, instance: Link, **kwargs: dict):
    Link.objects.fix_order_holes(instance)


@receiver(post_delete, sender=List)
def on_list_delete(sender, instance: List, **kwargs: dict):
    List.objects.fix_order_holes(instance)
