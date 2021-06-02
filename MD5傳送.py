import random
import hashlib as hb 
from pyDes import des, CBC, PAD_PKCS5 # des
import base64
import json

path = 'D:\Gitinit\docker-compose-DB\MD5test.txt'#文檔路徑
KEY='U0724023' # key 通常是 8bytes for DES 16/24 for triple 

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789' #random範圍
length = len(chars)-1

str = ''
num = 0
alphalow = 0
alphaup = 0

for i in range(1000):
    str+=chars[random.randint(0,length)]
    if str[i].islower(): #大寫
        alphalow+=1
    elif str[i].isupper():#小寫
        alphaup+=1
    else:
        num+=1
print ( str,"\n\nAlpha upper",alphaup,"| Alpha lower",alphalow,"| Number" ,num,"\n")

# 訊息摘要 md5 產生 128bits 0/1 會以 32bits個hex顯示
MD=(hb.md5(str.encode("utf-8"))).hexdigest()# 訊息摘要
print ("訊息摘要 (md5)",MD)
'''
binary 的方式 =>先從 16轉成 integer 再轉bin
ad = int(MD,16)
print (bin(ad))
'''

#github
#https://github.com/twhiteman/pyDes
#pydes教學
#https://malagege.github.io/blog/2015/04/26/logdown/2015-04-26-python-use-pydespy-encryption-and-decryption/
#CBC EBC
#https://notes.andywu.tw/2019/%E5%AF%86%E7%A2%BC%E7%9A%84%E5%8A%A0%E5%AF%86%E6%A8%A1%E5%BC%8Fecb-cbc-cfb-ofb-ctr/
#(key,mode,initial value, pad , padmode)
'''
CBC = 像是chain 要加密當前明文區塊需要前一個密文區塊
EBC = 直接切割明文block 切完以後 明文跟密文是1v1的關係
mode 為 CBC時候 需要有個IV向量
'''
iv = "".join(random.sample('0123456789',8))#list >> str 用join
k = des(KEY , CBC , iv , pad=None , padmode=PAD_PKCS5)
#加密 出來是 object的樣式
en = k.encrypt(MD)

ba = (base64.b64encode(en).decode("utf-8"))
print ("訊息摘要加密(DES): %r" % ba)
#print ("Decrypted: %r" % k.decrypt(en))

'''
#要消除b '' 只需要decode
de= k.decrypt(en)
de =de.decode("utf-8")
print(de)
'''

#https://jenifers001d.github.io/2019/12/11/Python/learning-Python-day9/
#寫成json檔 比較好操作
lines = {"str":str,'MD5':MD,'DES':ba,'KEY':KEY,'iv':iv}
#如果會忘記 close 可以改用 with as
with open(path,'w') as f:
    json.dump(lines,f)
    