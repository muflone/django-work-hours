FROM python:3.9-slim-buster

# App information
ENV app_name django-work-hours
ENV app_version 0.3.1

# Container metadata
LABEL maintainer="ilmuflone"
LABEL maintainer_email="muflone@muflone.com"
LABEL app_name="Django Work Hours"
LABEL app_version="${app_version}"

# Install and execute application
ADD "https://github.com/muflone/${app_name}/archive/${app_version}.tar.gz" "/tmp/${app_name}-${app_version}.tar.gz"
RUN tar xzf "/tmp/${app_name}-${app_version}.tar.gz" -C "/tmp" && \
    rm "/tmp/${app_name}-${app_version}.tar.gz" && \
    mv "/tmp/${app_name}-${app_version}" "/app"
COPY "settings_container.py" "/app/project/"
COPY "launch.sh" "/app/"
COPY "wait-for-it.sh" "/app/"
RUN apt-get update && \
    apt-get install --yes --no-install-recommends default-libmysqlclient-dev build-essential gettext && \
    echo "SECRET_KEY = '$(date +%s | sha256sum | base64 | head -c 50)'" >> "/app/project/settings_container.py" && \
    pip install -r /app/requirements.txt && \
    pip install mysqlclient && \
    apt-get autoremove --yes default-libmysqlclient-dev build-essential && \
    apt-get install --yes --no-install-recommends libmariadb3 && \
    rm -rf /var/lib/apt/lists/*
EXPOSE 8080/tcp
CMD ["bash", "/app/launch.sh", "8080"]

