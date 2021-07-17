import time
import requests
import hashlib
import urllib
import random
import json

to = ["zh", "en", "yue", "wyw", "jp", "kor", "fra", "spa", "th", "ara", "ru", "pt", "de", "it", "el", "nl", "pl", "bul",
      "est", "dan", "fin", "cs", "rom", "slo", "swe", "hu", "cht", "vie"]

print("WELCOME TO GRASS BUILDER")
query = input("WHAT GRASS DO YOU WANT TO GET\n")
print("YOU MIGHT HAVE TO WAIT 20s TO GET YOUR GRASS")


def getURL(toLang, q):
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥
    myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    fromLang = 'auto'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    return myurl


def getResult(s):
    global query
    rand = random.randint(0, 27)
    URL = getURL(to[rand], s)
    req = requests.get(URL)
    res = json.loads(req.text)
    query = res['trans_result'][0]['dst']
    print("THIS TIME'S QUERY:", query)
    time.sleep(1)


for i in range(20):
    getResult(query)

r = requests.get(getURL('zh', query))
result = json.loads(r.text)['trans_result'][0]['dst']
print("THIS IS YOUR GRASS: ")
print(result)
