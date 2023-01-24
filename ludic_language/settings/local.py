from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]']
SECRET_KEY = os.getenv("SECRET_KEY")


INSTALLED_APPS = INSTALLED_APPS + ['django_extensions', ]
