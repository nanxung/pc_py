import requests
import json
import re
import random
import pytesseract
from PIL import Image



req=requests.Session()
user_agent = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ']

header={
    'X-Requested-With': 'XMLHttpRequest',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':random.choice(user_agent),
    'Host': 'wenshu.court.gov.cn'
}

postData={
    'Param':'案件类型:民事案件,裁判年份:2017,法院层级:中级法院',
    'Index':1,
    'Page':20,
    'Order':'法院层级',
    'Direction':'asc',

}

url0='http://wenshu.court.gov.cn/List/ListContent'
url1='http://wenshu.court.gov.cn/User/ValidateCode'
url2='http://wenshu.court.gov.cn/Content/CheckVisitCode'

#获取验证码并识别
r=req.post(url1,headers=header,timeout=60)

with open("a.jpg",'wb') as w:
     w.write(r.content)

image=Image.open('a.jpg')
code=pytesseract.image_to_string(image)
print(code)

#验证验证码
data={
    'ValidateCode': code
}

r=req.post(url2,data=data,headers=header,timeout=60)
print(r.text)

print(req.post(url='http://wenshu.court.gov.cn/ValiCode/GetCode',headers=header,timeout=60).text)

t=req.post(url=url0,data=postData,headers=header,timeout=60)
print(t.text)