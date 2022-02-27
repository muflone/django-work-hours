# Django Work Hours
[![Travis CI Build Status](https://img.shields.io/travis/com/muflone/django-work-hours/master.svg)](https://www.travis-ci.com/github/muflone/django-work-hours)
[![CircleCI Build Status](https://img.shields.io/circleci/project/github/muflone/django-work-hours/master.svg)](https://circleci.com/gh/muflone/django-work-hours)

**Description:** A Django application to manage the employees work hours 

**Copyright:** 2022 Fabio Castelli (Muflone) <muflone@muflone.com>

**License:** GPL-3+

**Source code:** https://github.com/muflone/django-work-hours

**Documentation:** http://www.muflone.com/django-work-hours/

# Description

Django work-hours is a Django application to manage employees work hours.

Containers or virtual environments' usage is **highly encouraged** to
isolate from any other Python package installed in your system.

---

# Django Work Hours server

To install the Django Work Hours server you need to first install the
system requirements and then following the below installation
instructions.  

## System Requirements

The Python dependencies for the server part are listed in the
`requirements.txt` file.

* Python >= 3.9
* Django 4.0.x (https://pypi.org/project/Django/)
* Django Admin List Filter Dropdown (https://pypi.org/project/django-admin-list-filter-dropdown/)
* Django Bootstrap Date-Picker Plus (https://pypi.org/project/django-bootstrap-datepicker-plus/)

Additional optional dependencies might be needed to use your desired
database.

## Settings file

You can set up your desired settings by editing the `project/settings.py`
file or by creating a new file into the `project` directory with the
following:

```python
from .settings import *

# Your_settings will go here
```

You can then specify the settings file using `--settings project.file`
flag or by setting the `DJANGO_SETTINGS_MODULE` environment variable.

```shell
export DJANGO_SETTINGS_MODULE=project.my_settings
```

## Database setup

You can use any database that is supported by Django and setup it
in a settings file.

For example to set up a SQLite database you can use the following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/path/to/your-database.sqlite3',
    }
}
```

When you're ready with your database setup you can create all the
required tables and data using the following command:

```shell
python manage.py migrate
```

## Create a new Administrator account

Before you can start to use the application you need to create a new
administrator account using the following:

```shell
python manage.py createsuperuser
```

And following the instructions.

## Starting the server

The Django application should be served through a WSGI server like
gunicorn. For testing purposes only you can use the integrated Django
debug server.

To start the integrated Django debug server you can use:

```shell
python manage.py runserver 0.0.0.0:8000
```

This will start a server running on the TCP port 8000.

**Please remember to use the integrated Django debug server for
testing purposes only** as it's not a secure, fast and reliable
server to run Python applications.

## Usage

When you're ready open a web browser and navigate the page you set
during the server startup (e.g. http://localhost:8000/admin)
