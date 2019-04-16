# vangogh

just like google photos, build a private photo gallery on web.

* development system: windows 7
* language: python3
* database: sqlite3
* backend web framework: django
* frontend web framework: Vue
* deep learning: tensorflow
* deploy container: Docker

run environment:

environment variables:

* BAIDU_MAP_SK Baidu Map secret key

django create tables：

```shell
python manage.py makemigrations photo person album

python manage.py migrate
```

Docker build:

```shell
docker build --tag vangogh .
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

