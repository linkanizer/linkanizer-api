from __future__ import absolute_import, unicode_literals
from celery import shared_task

import requests
from bs4 import BeautifulSoup

from .models import Link


@shared_task()
def scrape_link_metadata(link_id):
    link = Link.objects.get(pk=link_id)
    r = requests.get(link.url)

    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        link.title = soup.title.string
        link.save()

    return True
