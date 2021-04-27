import pymysql
dbhost='https://justtry.406.csie.nuu.edu.tw'
dbuser='root'
dbport=3306
dbpass='nuuCSIE406'
dbname='phpmyadmin'

try:
    db=pymysql.connect(host=dbhost,user=dbuser,port=dbport,password=dbpass,database=dbname)
    print("数据库连接成功")
except pymysql.Error as e:
    print("数据库连接失败："+str(e))
