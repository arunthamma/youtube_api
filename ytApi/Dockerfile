FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ytApi.settings

RUN apt-get update && \
    apt-get -y install cron \
    libcairo2 gir1.2-gtk-3.0

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code

CMD ./manage.py migrate --settings=$SETTINGS_TO_RUN && \
    ./manage.py collectstatic --noinput && \
    service cron start && \
    newrelic-admin run-program gunicorn --bind 0.0.0.0:8080 --access-logfile - {{cookiecutter.app_name}}.wsgi:application
