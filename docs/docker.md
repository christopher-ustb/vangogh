win7使用docker toolbox安装docker，需要先将windows文件夹共享给docker-machine:一个运行在virtual box中的linux服务器才能向docker挂在磁盘。

https://blog.shahinrostami.com/2017/11/docker-toolbox-windows-7-shared-volumes/

nginx

https://hub.docker.com/_/nginx

Hosting some simple static content

```
docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx
```
