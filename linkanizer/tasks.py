from celery import shared_task

import metadata_parser

from .models import Link


@shared_task()
def scrape_link_metadata(link_id):
    link = Link.objects.get(pk=link_id)

    page = metadata_parser.MetadataParser(url=link.url)

    title = page.get_metadata("title")
    imageUrl = page.get_metadata_link("image")
    description = page.get_metadata("metadata")

    if title:
        link.title = title

    if imageUrl:
        link.imageUrl = imageUrl

    if description:
        link.description = description

    link.save()

    return True
