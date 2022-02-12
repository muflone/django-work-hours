from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/django-work-hours.sqlite3',
    }
}

ALLOWED_HOSTS = ['localhost', 'backend']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']
DEBUG=False

