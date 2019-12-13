from .common import *  # noqa

ALLOWED_HOSTS = ["*"]

# Database

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "/code/prod.sqlite3"}
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "change me!"
