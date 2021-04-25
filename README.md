# docker-compose-DB
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