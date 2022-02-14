# Installation as a docker container

Installing Django Work Hours as a docker container is pretty straightforward as
it exists as official image in the Docker Hub at the URL
https://hub.docker.com/repository/docker/ilmuflone/django-work-hours

---

## Setup with MySQL/MariaDB

You can compose a very simple docker stack using compose.

First prepare a settings file for the container with the name
**new_settings_container.py**:

```python
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
```

Then create a nginx configuration file like the following **nginx.conf**:

```
upstream backend {
  ip_hash;
  server backend:8080;
}

server {
  location /static/ {
    autoindex on;
    alias /static/;
  }

  location / {
    proxy_pass http://backend/;
  }
  listen 8000;
  server_name localhost;
}
```

This configuration will allow nginx to serve the port 8000 and directly handle
the `/static` URL and pass everything else to the backend on the port 8080.

Create a `database_root.env` file with the password for the root MySQL user:
```ini
MYSQL_ROOT_PASSWORD=root_password
```

Create another `database.env` file with the details about the new database,
user and password

```ini
MYSQL_HOST=django-work-hours-mysql_db
MYSQL_PORT=3306
MYSQL_DATABASE=workhours
MYSQL_USER=workhours
MYSQL_PASSWORD=workhours_password
```
Here follows the **docker-compose.yaml** for creating the containers:

```yaml
version: '3'

services:
  web:
    container_name: django-work-hours-mysql_web
    image: nginx:1.21.3-alpine
    ports:
      - 8000:8000/tcp
    depends_on:
      - backend
    volumes:
      - ./static:/static
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ./logs:/var/log/nginx

  backend:
    container_name: django-work-hours-mysql_backend
    image: ilmuflone/django-work-hours:0.2.2-mysql
    env_file:
      - ./database.env
    environment:
      - SERVER_PORT=8080
    expose:
      - 8080
    depends_on:
      - database
    volumes:
      - ./static:/app/static
      - ./new_settings_container.py:/app/project/settings_container.py

  database:
    container_name: django-work-hours-mysql_db
    image: mysql:5
    env_file:
      - ./database.env
      - ./database_root.env
    volumes:
      - ./db:/var/lib/mysql
```

- The container `django-work-hours-mysql_web` will run nginx to serve the HTTP
requests and the `/static` URL with the static files.
- The container `django-work-hours-mysql_backend` will run the Django
application to process the requests passed from nginx.
- The container `django-work-hours-mysql_db` will run the database server used
from the backend application.

The nginx server will listen on the port 8000 and the backend server will listen
on the port 8080. The backend port 8080 won't be published on the docker host so
no connections will be allowed to it.

Let's create three folders: **db** for keeping the database data, **static**
for serving the static files between Django Work Hours and nginx and **logs**
for saving the nginx logs.

Finally you can build your stack using: `docker-compose up -d`.

When your stack is ready you can create a superuser using:

    docker exec -it django-work-hours-mysql_backend \
      python /app/manage.py createsuperuser \
      --settings project.settings_container

Point your web browser on http://your-ip:8000/ and you'll be welcomed from the
login page. If you want to access the administration console surf towards
http://your-ip:8000/admin
