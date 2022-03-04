# Installation as a docker container

Installing Django Work Hours as a docker container is pretty straightforward as
it exists as official image in the Docker Hub at the URL
https://hub.docker.com/repository/docker/ilmuflone/django-work-hours

---

## Setup with SQLite

You can compose a very simple docker stack using compose.

First prepare a settings file for the container with the name
**new_settings_container.py**:

```python
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

Here follows the **docker-compose.yaml** for creating the containers:

```yaml
version: '3'

services:
  web:
    container_name: django-work-hours_web
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
    container_name: django-work-hours_backend
    image: ilmuflone/django-work-hours:0.3.2
    environment:
      - SERVER_PORT=8080
    expose:
      - 8080
    volumes:
      - ./static:/app/static
      - ./database.sqlite3:/var/lib/django-work-hours.sqlite3
      - ./new_settings_container.py:/app/project/settings_container.py
```

- The container `django-work-hours_web` will run nginx to serve the HTTP requests
and the `/static` URL with the static files.
- The container `django-work-hours_backend` will run the Django application to
process the requests passed from nginx.

The nginx server will listen on the port 8000 and the backend server will listen
on the port 8080. The backend port 8080 won't be published on the docker host so
no connections will be allowed to it.

Let's create an empty **database.sqlite3** file and also two folders: **static**
for serving the static files between Django Work Hours and nginx and **logs**
for saving the nginx logs.

Finally you can build your stack using: `docker-compose up -d`.

When your stack is ready you can create a superuser using:

    docker exec -it django-work-hours_backend \
      python /app/manage.py createsuperuser \
      --settings project.settings_container

Point your web browser on http://your-ip:8000/ and you'll be welcomed from the
login page. If you want to access the administration console surf towards
http://your-ip:8000/admin
