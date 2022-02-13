import os

from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['MYSQL_HOST'],
        'PORT': os.environ['MYSQL_PORT'],
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
    }
}

ALLOWED_HOSTS = ['localhost', 'backend']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']
DEBUG=False

