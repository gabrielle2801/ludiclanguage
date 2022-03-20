import django_heroku
from .base import *
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SECRET_KEY = os.getenv("SECRET_KEY")
sentry_sdk.init(
    dsn="https://879029efb2504d0591680414d287ccab@o1171139.ingest.sentry.io/6265263",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': '5432'
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'ludic_language.storage.S3Storage'
# Activate Django-Heroku.
django_heroku.settings(locals())
