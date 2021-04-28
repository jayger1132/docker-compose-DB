# docker-compose-DB
### 一開始在安裝 pymysql 時需要先確定有安裝visual studio C v14
## pymysql 這個就好版本 (py3.0以上使用)
# mysql-python  這個在搞 安裝問題很多

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
## python
#### 查詢回來的方式 是用矩陣的方式 配置每個name
```py
sql = "SELECT * FROM account WHERE account = '%s'" % (account)
try:
    #cursor.execute執行 sql動作
    cursor.execute(sql)
    results = cursor.fetchone()
    print (results[1])
    #db.commit 提交到DB執行
    db.commit()
except:
       db.rollback()
```
#### 要輸入變數 INSERT必須為雙引號 
```py
sql = "INSERT INTO account(account,password) VALUES ('%s' , '%s')" %(account, password)
```
#### update的寫法
```py
sql = "UPDATE account SET date = '%s' , multiple = 1  WHERE account = '%s'" % (localtime,account)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
```

#### py時間的寫法
```py
#time.time() 轉換出來是秒的形式
#localtime 是 struct型態 strftime是轉成字串型態
localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
```
#### 時間的比較方式
```py
from datetime import datetime, timedelta
#現在時間
current_date = datetime.now()
#更新密碼後超過 30秒就要重新設定密碼
overtime = results[0]+timedelta(minutes=30)
if current_date > overtime:
    print("your password is too old to keep safely please renew your password")
```
#### hash一個以md5為加密方法的加密
```py
#轉成密文
password = hb.md5(password.encode("utf-8"))
#輸出密文的值 如果沒有轉換他會單純顯示md5方法
password = password.hexdigest()
```
## 參考資料
#### docker-compose.yml的详细解释与说明
https://blog.csdn.net/yb546822612/article/details/105276164
#### 官網
https://docs.docker.com/compose/compose-file/compose-file-v2/
#### port 介紹
https://myctw.github.io/post/df5.html
#### 時間比較
https://www.delftstack.com/zh-tw/howto/python/python-compare-dates/
#### hash的各種方法
https://www.cnblogs.com/cwp-bg/p/10256640.html

## 可以不用 撰寫port的方式 讓他自動設定 port PMA_HOST depend(資料在 nextcloud 跟 smarthome資料庫)待完成....
