import pymysql
import time
dbhost='justtry.406.csie.nuu.edu.tw'
dbuser='root'
dbport=33060
dbpass='nuuCSIE406'
dbname='account'
"""
查詢回來的方式 是用矩陣的方式 配置每個name
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
"""

try:
    db=pymysql.connect(host=dbhost,user=dbuser,port=dbport,password=dbpass,database=dbname)
    print("連結成功")
    cursor = db.cursor()
except pymysql.Error as e:
    print("連線失敗"+str(e))

log = input ('please enter log in or log up \n')

# 要輸入變數 INSERT必須為雙引號 
#sql = "INSERT INTO account(account,password) VALUES ('%s' , '%s')" %(account, password)

if (log == "log in"):
    #print("in")
    account= input("please enter account \n")
    
#註冊
elif (log == "log up"):
    #print("up")
    account= input("please enter account \n")
    sql = "SELECT * FROM account WHERE account = '%s'" % (account)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
    except:
       db.rollback()
  
    while results != None :
        account = input("please enter another account \n")
        sql = "SELECT * FROM account WHERE account = '%s'" % (account)
        try:
            cursor.execute(sql)
            results = cursor.fetchone()
        except:
            db.rollback()
    ##還需要再寫加密的部分
    
    password = input("please enter password include upper,lower and number \n")
    #判斷大小寫以及數字
    while True:
        flagU = 0 
        flagL = 0
        flagN = 0
        if len(password) <= 8 or password.isalnum() != True :
            password = input("please enter correct password \n")
        for test in password:
            if ord(test) >= 97 and ord(test)<=122 :
                flagL = 1
            if ord(test) >= 65 and ord(test)<=90 :
                flagU = 1
            if ord(test) >=48 and ord(test)<=57:
                flagN = 1
        if flagL==1 and flagU==1 and flagN==1:
            ## 二次輸入密碼
            password2 = input("double check password \n")
            if password == password2:
                break
            else:
                print("they are different please enter password again")
                continue
        else:
            password = input("please enter correct password \n")
    
    # 記錄目前時間       
    localtime = time.localtime()
    localtime=time.strftime("%Y-%m-%d %I:%M:%S", localtime)
    
    sql = "INSERT INTO account(account,password,date) VALUES ('%s' , '%s' , '%s')" %(account, password,localtime)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    #print ("now")