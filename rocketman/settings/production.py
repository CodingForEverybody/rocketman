import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = False
SECRET_KEY = ''  # @todo get a key from here https://miniwebtool.com/django-secret-key-generator/
ALLOWED_HOSTS = ['localhost', 'yourwebsite.com']  # @todo add your website url in here
cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx2',
        "HOST": 'localhost',
        "PORT": "",
    }
}


sentry_sdk.init(
    dsn="",  # @todo add your Sentry DSN key in here
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
