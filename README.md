# vangogh

just like google photos, build a private photo gallery on web.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software

* python3
* pip
* nodejs
* docker(need to production build)

### Installing

1. goto project directory,and setup virtual env

```shell
python -m venv venv
```

2. install pip requirements

```shell
pip install -r requirements.txt
```

3. set enviroment variables

* VANGOGH_BAIDU_MAP_AK: baidu map access key
* VANGOGH_BAIDU_MAP_SK: baidu map secret key

4. create tables by django models

```
python manage.py makemigrations photo person album

python manage.py migrate
```

5. run django dev server

```shell
python manage.py runserver
```

## Deployment

build docker image from dockerfile and code:

```shell
docker build -t christopher-ustb/vangogh:latest .
```

tips:

This docker build progress needs a lot of memory(>3GB). If your docker machine(windows7/Mac) don't have enough physical memory, you should add some more swap file, otherwise, your C++ compiler will end up with an internal error because of memory insufficient.

add swap file command:

```shell
export SWAPFILE=/mnt/sda1/swapfile
sudo dd if=/dev/zero of=$SWAPFILE bs=1024 count=4194304
sudo mkswap $SWAPFILE
sudo chmod 600 $SWAPFILE
sudo swapon $SWAPFILE
swapon -s
```

docker run the image

```shell
docker run -t christopher-ustb/vangogh
```

## Built With

* [Django](https://www.djangoproject.com/) - backend web framework
* sqlite3 - database
* [Vue](https://vuejs.org) - frontend web framework
* [Docker](https://www.docker.com/) - deploy container tool

## Authors

* Christopher Wang

## Thanks

* Product inspiration by Google photos and Xiaomi Cloud photos
