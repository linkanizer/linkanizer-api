from .common import *  # noqa

ALLOWED_HOSTS = ["*"]

DEBUG = False

# Database

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "/code/prod.sqlite3"}
}
