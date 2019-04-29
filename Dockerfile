FROM python:3.7-slim

RUN mkdir /root/vangogh
COPY requirements.txt /root/vangogh
WORKDIR /root/vangogh

RUN set -ex \
    && BUILD_DEPS=" \
        build-essential \
        libpcre3-dev \
        libpq-dev \
        cmake \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && python3.7 -m venv /venv \
    && /venv/bin/pip install -U pip \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt \
    && /venv/bin/pip install --no-cache-dir uwsgi
    \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

COPY . /root/vangogh

ENV UWSGI_WSGI_FILE=vangogh/wsgi.py

# Base uWSGI configuration (you shouldn't need to change these):
ENV UWSGI_VIRTUALENV=/venv UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Number of uWSGI workers and threads per worker (customize as needed):
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

EXPOSE 8000

RUN mkdir -p /var/log/vangogh && mkdir -p /var/lib/vangogh/db

VOLUME /var/log/vangogh
VOLUME /var/lib/vangogh

ENTRYPOINT ["/root/vangogh/docker-entrypoint.sh"]

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--show-config"]

# env VANGOGH_BAIDU_MAP_AK/VANGOGH_BAIDU_MAP_SK
