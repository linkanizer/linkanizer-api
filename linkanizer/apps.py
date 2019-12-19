from django.apps import AppConfig


class LinkanizerConfig(AppConfig):
    name = "linkanizer"

    def ready(self):
        from . import signals
