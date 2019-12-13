from .common import *  # noqa

DEBUG = True

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "n3ya)e3j#4&^!h67w-u2oc)w#a$r9+2fqy+!#*oquwo^ow0lo#"
