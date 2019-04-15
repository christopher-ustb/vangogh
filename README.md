# vangogh

just like google photos, build a private photo gallery on web.

* system: windows 7
* language: python3
* database: sqlite3
* backend web framework: django
* frontend web framework: Vue
* deep learning: tensorflow
* deploy container: Docker

运行环境：

环境变量：

* BAIDU_MAP_SK 百度地图SK

建表：

```shell
python manage.py makemigrations photo person album

python manage.py migrate
```