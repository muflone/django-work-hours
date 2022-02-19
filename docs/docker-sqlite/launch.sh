#!/bin/bash

cd /app
django-admin compilemessages
export DJANGO_SETTINGS_MODULE='project.settings_container'
python manage.py collectstatic --no-input --no-color
python manage.py migrate
python manage.py runserver 0.0.0.0:${SERVER_PORT:-8080}

