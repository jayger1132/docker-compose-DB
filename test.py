import pymysql
import time
import hashlib as hb
import sys
from datetime import datetime, timedelta

dbhost='justtry.406.csie.nuu.edu.tw'
dbuser='root'
dbport=33060
dbpass='nuuCSIE406'
dbname='account'


try:
    db=pymysql.connect(host=dbhost,user=dbuser,port=dbport,password=dbpass,database=dbname)
    print("連結成功")
    cursor = db.cursor()
except pymysql.Error as e:
    print("連線失敗"+str(e))
 
#轉換出來是秒的形式
#timeString = int(time.time()) 

log = input ('please enter log in or log up \n')

"""account ="jayger789"
sql = "SELECT register FROM account WHERE account = '%s'" % (account)
try:
    cursor.execute(sql)
    results = cursor.fetchone()
except:
    db.rollback()
print(results[0])

current_date = datetime.now()
previous_date = results[0] - timedelta(days=1)
if current_date > previous_date:
    print("your password is too old to keep safely please renew your password")
    
"""

# 要輸入變數 INSERT必須為雙引號 
#sql = "INSERT INTO account(account,password) VALUES ('%s' , '%s')" %(account, password)

if (log == "log in"):
    #print("in")
    account = input("please enter account \n")
    password = input("please enter password \n")
    #print (account , password)
    sql = "SELECT account , password , date FROM account WHERE account = '%s'" % (account)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
    except:
        db.rollback()
    #print (results[0],results[1],results[2])
    #判斷登入資料是否正確
    count = 1 
    if results == None :
        while(count<=3):
            #判斷是否超過三次
            #print("now")
            if(count ==3):
                print("enter more than 3 times \n")
                sys.exit()
            else:
                count+=1
            print("please enter correct account or password")
            
            account = input ("please enter  account \n" )
            password = input ("please enter  password \n")
            sql = "SELECT account , password , date FROM account WHERE account = '%s'" % (account)
            try:
                cursor.execute(sql)
                results = cursor.fetchone()
            except:
                db.rollback()
        
            password = hb.md5(password.encode("utf-8"))
            password = password.hexdigest()
            if(results!=None):
                if (password == results[1]):
                    print ("welcome")
                    print ("last log in at ",results[2])
                    #判斷有無重複登入
                    sql = "SELECT multiple FROM account WHERE account = '%s'" % (account)
                    try:
                        cursor.execute(sql)
                        results = cursor.fetchone()
                    except:
                        db.rollback()
                    #print (results)
                    if results[0] == 1 :
                        print ("multiple log in")
                    #更新登入時間
                    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    sql = "UPDATE account SET date = '%s' , multiple = 1  WHERE account = '%s'" % (localtime,account)
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()
                    break
                else:
                    continue
    else:
        password = hb.md5(password.encode("utf-8"))
        password = password.hexdigest()
        if (password == results[1]):
                print ("welcome")
                print ("last log in at ",results[2])
                #判斷有無重複登入
                sql = "SELECT multiple FROM account WHERE account = '%s'" % (account)
                try:
                    cursor.execute(sql)
                    results = cursor.fetchone()
                except:
                    db.rollback()
                #print (results)
                if results[0] == 1 :
                    print ("multiple log in")
                #更新登入時間
                localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                sql = "UPDATE account SET date = '%s' , multiple = 1  WHERE account = '%s'" % (localtime,account)
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
        else: 
            while(count <= 3):
                #判斷是否超過三次
                #print("now")
                if(count == 3):
                    print("enter more than 3 times \n")
                    sys.exit()
                else:
                    count+=1
                print("please enter correct account or password")
                
                account = input ("please enter  account \n" )
                password = input ("please enter  password \n")
                sql = "SELECT account , password , date FROM account WHERE account = '%s'" % (account)
                try:
                    cursor.execute(sql)
                    results = cursor.fetchone()
                except:
                    db.rollback()
                    
                password = hb.md5(password.encode("utf-8"))
                password = password.hexdigest()
                if(results!=None):
                    if (password == results[1]):
                        print ("welcome")
                        print ("last log in at ",results[2])
                        #判斷有無重複登入
                        sql = "SELECT multiple FROM account WHERE account = '%s'" % (account)
                        try:
                            cursor.execute(sql)
                            results = cursor.fetchone()
                        except:
                            db.rollback()
                        #print (results)
                        if results[0] == 1 :
                            print ("multiple log in")
                            
                        #更新登入時間
                        localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                        sql = "UPDATE account SET date = '%s' , multiple = 1  WHERE account = '%s'" % (localtime,account)
                        try:
                            cursor.execute(sql)
                            db.commit()
                        except:
                            db.rollback()
                        break
                    else:
                        continue
        
            
    
    #詢問是否要 更改密碼 或是 登出  
    while True :
        #超過時間需要重新設定密碼
        sql = "SELECT register FROM account WHERE account = '%s'" % (account)
        try:
            cursor.execute(sql)
            results = cursor.fetchone()
        except:
            db.rollback()
        #現在時間
        current_date = datetime.now()
        #更新密碼後超過 30秒就要重新設定密碼
        overtime = results[0]+timedelta(minutes=30)
        if current_date > overtime:
            print("your password is too old to keep safely please renew your password")
            flag = False
            while True:
                if flag == False:
                    
                    oldpassword = input("please enter old password \n")
                    newpassword = input("please enter new password include upper,lower and number \n")
                    password2 = input("double check new password \n")            
                    
                    oldpassword = hb.md5(oldpassword.encode("utf-8"))
                    oldpassword = oldpassword.hexdigest()
                    
                    if oldpassword == password:
                        while True:
                            flagU = 0 
                            flagL = 0
                            flagN = 0
                            if len(newpassword) <= 8 or newpassword.isalnum() != True :
                                newpassword = input("please enter correct newpassword \n")
                                continue
                            for test in newpassword:
                                if ord(test) >= 97 and ord(test)<=122 :
                                    flagL = 1
                                if ord(test) >= 65 and ord(test)<=90 :
                                    flagU = 1
                                if ord(test) >=48 and ord(test)<=57:
                                    flagN = 1
                            if flagL==1 and flagU==1 and flagN==1:
                                ## 二次輸入密碼
                                if newpassword == password2:
                                    newpassword = hb.md5(newpassword.encode("utf-8"))
                                    newpassword = newpassword.hexdigest()
                                    
                                    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                                    sql = "UPDATE account SET password = '%s' , register = '%s'  WHERE account = '%s'" % (newpassword,localtime,account)
                                    try:
                                        cursor.execute(sql)
                                        db.commit()
                                    except:
                                        db.rollback()
                                    #更新完了
                                    print("renew sucessful")
                                    flag = True
                                    break
                                else:
                                    print("they are different please enter new password again")
                                    continue
                            else:
                                newpassword = input("please enter correct new password \n")
                    else:
                        print("old password is not correct")
                        break
                else:
                    break
        #確認不用因為密碼太舊更新密碼
        else:
            action = input("if want to change password please enter \"renew\" or want to log out enter \"log out\"\n")
            if action == "log out" :
                sql = "UPDATE account SET multiple = 0  WHERE account = '%s'" % (account)
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                print("log out sucessful")
                sys.exit()
            elif action == "renew" :
                #判斷是不是更新完了
                flag = False
                while True:
                    if flag == False:
                        
                        oldpassword = input("please enter old password \n")
                        newpassword = input("please enter new password include upper,lower and number \n")
                        password2 = input("double check new password \n")            
                        
                        oldpassword = hb.md5(oldpassword.encode("utf-8"))
                        oldpassword = oldpassword.hexdigest()
                        
                        if oldpassword == password:
                            while True:
                                flagU = 0 
                                flagL = 0
                                flagN = 0
                                if len(newpassword) <= 8 or newpassword.isalnum() != True :
                                    newpassword = input("please enter correct newpassword \n")
                                    continue
                                for test in newpassword:
                                    if ord(test) >= 97 and ord(test)<=122 :
                                        flagL = 1
                                    if ord(test) >= 65 and ord(test)<=90 :
                                        flagU = 1
                                    if ord(test) >=48 and ord(test)<=57:
                                        flagN = 1
                                if flagL==1 and flagU==1 and flagN==1:
                                    ## 二次輸入密碼
                                    if newpassword == password2:
                                        newpassword = hb.md5(newpassword.encode("utf-8"))
                                        newpassword = newpassword.hexdigest()
                                        
                                        localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                                        sql = "UPDATE account SET password = '%s' , register = '%s'  WHERE account = '%s'" % (newpassword,localtime,account)
                                        try:
                                            cursor.execute(sql)
                                            db.commit()
                                        except:
                                            db.rollback()
                                        #更新完了
                                        print("renew sucessful")
                                        flag = True
                                        break
                                    else:
                                        print("they are different please enter new password again")
                                        continue
                                else:
                                    newpassword = input("please enter correct new password \n")
                        else:
                            print("old password is not correct")
                            break
                    else:
                        break
    #print("now")
#註冊
elif (log == "log up"):
    #print("up")
    account= input("please enter account \n")
    sql = "SELECT account FROM account WHERE account = '%s'" % (account)
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
    except:
       db.rollback()

    while results != None :
        account = input("please enter another account \n")
        sql = "SELECT account FROM account WHERE account = '%s'" % (account)
        try:
            cursor.execute(sql)
            results = cursor.fetchone()
        except:
            db.rollback()
    
    password = input("please enter password include upper,lower and number \n")
    #判斷大小寫以及數字
    while True:
        flagU = 0 
        flagL = 0
        flagN = 0
        if len(password) <= 8 or password.isalnum() != True :
            password = input("please enter correct password \n")
            continue
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
            
    # hash一個以md5為加密方法的加密
    password = hb.md5(password.encode("utf-8"))
    password = password.hexdigest()
    #輸出密文資料
    #print (password.hexdigest())
    
    #localtime 是 struct型態 strftime是轉成字串型態
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    
    
    
    sql = "INSERT INTO account(account,password,date,register,multiple) VALUES ('%s' , '%s' , '%s' ,'%s',0)" %(account, password,localtime,localtime)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print("register sucessful")
    #print ("now")
