# docker-compose-DB
## Ports: 能連到主機的這些 port 都能夠使用。
## expose: 僅能在此 docker-compose 內的 container 們使用。
### port phpmyadmin只是管理系統 mariadb才是真正的資料庫
```yml
# 主機 port:docker port 好處是讓對外的主機不會直接連到原始port
    ports:
      - "33060:3306"
```
### volumes 容器:本機目標地
```yml
volumes:
  # - / 這個斜槓不打 他抓不到 mariadb的service
      - /mariadb:/var/lib/mysql
```
## 參考資料
#### docker-compose.yml的详细解释与说明
https://blog.csdn.net/yb546822612/article/details/105276164
#### 官網
https://docs.docker.com/compose/compose-file/compose-file-v2/
#### port 介紹
https://myctw.github.io/post/df5.html