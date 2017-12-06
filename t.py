import requests
import json
import re
import random
import pytesseract
from PIL import Image
import random
def createGuid():
    return str(hex(int((1+random.random())*0x10000)))[3:]

def getid():
    return createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid()

guid=getid()
req=requests.Session()

user_agent = [
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ']

header={
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Connection':'keep-alive',
        # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95',
        'Host': 'wenshu.court.gov.cn'
}


data={
    'guid':guid
}
print(guid)
url='http://wenshu.court.gov.cn/ValiCode/GetCode'
number=req.post(url=url,data=data,headers=header).text
print(number)
req.get(url='http://wenshu.court.gov.cn/list/list/?sorttype=1&number={}&guid={}&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6&conditions=searchWord+2017+++%E8%A3%81%E5%88%A4%E5%B9%B4%E4%BB%BD:2017&conditions=searchWord+%E4%B8%AD%E7%BA%A7%E6%B3%95%E9%99%A2+++%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7:%E4%B8%AD%E7%BA%A7%E6%B3%95%E9%99%A2'.format(number,guid),headers=header)

vjkl5=req.cookies['vjkl5']
print(vjkl5)
vl5x=json.loads(req.get(url='http://172.16.143.50:2017/{}'.format(vjkl5)).text)['key']
print(vl5x)

# postData={
#     'Param':'案件类型:民事案件,裁判年份:2017,法院层级:中级法院',
#     'Index':1,
#     'Page':5,
#     'Order':'法院层级',
#     'Direction':'asc',
#    'guid':guid,
#     'vl5x':vl5x,
#    'number':number
#
# }
#
#
# # req.cookies['vjkl5']='46bc0289fff452cb6010c187367ef5b5a45f9d73'
#
url0='http://wenshu.court.gov.cn/List/ListContent'
# t=req.post(url=url0,data=postData,headers=header,timeout=6000)
# print(t.text)

print(req.cookies)
header__={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'ASP.NET_SessionId=ofjaviweghydtbty2rzw4ozv; Hm_lvt_3f1a54c5a86d62407544d433f6418ef5=1512373490,1512448767,1512533980; Hm_lpvt_3f1a54c5a86d62407544d433f6418ef5=1512573728; _gscu_2116842793=12373489ryjq8024; _gscs_2116842793=t12570769vkle5n32|pv:15; _gscbrs_2116842793=1; vjkl5=91b2a9fff712c4e017d180011d783481dc76df52',
'Host':'wenshu.court.gov.cn',
'Origin':'http://wenshu.court.gov.cn',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}

n=1
data__={
'Param':'案件类型:刑事案件,裁判年份:2017,法院层级:中级法院',
'Index':n,
'Page':'5',
'Order':'法院层级',
'Direction':'asc',
'vl5x':'40a889a7ddcf2c89bb69e9b6',
'number':'PU9TJ4YX',
'guid':'0dc2339d-1996-37980989-0bb8256d69fa',
}

with open('s.json','w') as w:
    while True:
        data__['Index']=n
        t=req.post(url=url0,data=data__,headers=header__,timeout=6000)
        if len(t.text)>100:
            w.write(t.text+"\n")
        else:
            break
        print(t.text)
        n+=1




'''
url1='http://wenshu.court.gov.cn/User/ValidateCode'
url2='http://wenshu.court.gov.cn/Content/CheckVisitCode'

#获取验证码并识别
r=req.get(url1,headers=header,timeout=60)
print(req.cookies['vjkl5'])

with open("a.jpg",'wb') as w:
     w.write(r.content)

image=Image.open('a.jpg')
code=pytesseract.image_to_string(image)

#验证验证码
data={
    'ValidateCode': code
}
r=req.post(url2,data=postData,headers=header,timeout=60)
print(req.cookies['vjkl5'])

t=req.post(url=url0,data=postData,headers=header,timeout=60)
print(t.text)
print(req.cookies['vjkl5'])
'''