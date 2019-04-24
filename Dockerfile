FROM python:3.7-slim

# RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
#COPY  sources.list /etc/apt/
# RUN  apt-get clean

# RUN apt-get -y update && apt-get install -y --fix-missing \
#     build-essential \
#     cmake \
#     gfortran \
#     git \
#     wget \
#     curl \
#     graphicsmagick \
#     libgraphicsmagick1-dev \
#     libatlas-dev \
#     libavcodec-dev \
#     libavformat-dev \
#     libboost-all-dev \
#     libgtk2.0-dev \
#     libjpeg-dev \
#     liblapack-dev \
#     libswscale-dev \
#     pkg-config \
#     python3-dev \
#     python3-numpy \
#     software-properties-common \
#     zip \
#     && apt-get clean && rm -rf /tmp/* /var/tmp/*

# RUN cd ~ && \
#     mkdir -p dlib && \
#     git clone -b 'v19.5' --single-branch https://github.com/davisking/dlib.git dlib/ && \
#     cd  dlib/ && \
#     python3 setup.py install --yes USE_AVX_INSTRUCTIONS

RUN mkdir /root/vangogh
COPY requirements.txt /root/vangogh
WORKDIR /root/vangogh
# RUN pip3 install -r requirements.txt
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

# CMD ["python", "manage.py", "runserver"]

RUN mkdir -p /var/log/vangogh && mkdir -p /var/lib/vangogh/db

ENTRYPOINT ["/root/vangogh/docker-entrypoint.sh"]

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--show-config", "--uid", "root"]
