import pymysql
dbhost='justtry.406.csie.nuu.edu.tw'
dbuser='root'
dbport=33060
dbpass='nuuCSIE406'
dbname='test'

try:
    db=pymysql.connect(host=dbhost,user=dbuser,port=dbport,password=dbpass,database=dbname)
    print("数据库连接成功")
except pymysql.Error as e:
    print("数据库连接失败："+str(e))
