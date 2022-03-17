from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]']
SECRET_KEY = os.getenv("SECRET_KEY")


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

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
