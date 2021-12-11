import pandas as pd
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

dt = pd.read_excel('result.xlsx','Sheet1')
stars = set()
for names in dt['Starring']:
    if names is not np.nan:
        for name in str(names).replace('、',',').replace('，',',').split(','):
            stars.add(name)
            
url = "https://s.weibo.com/weibo?q="
headers = {
"Host": "s.weibo.com",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate, br",
"Connection": "keep-alive",
"Cookie": "www.52jingsai.com,widget.weibo.com,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWbjVd7EgcvSe75XM2kBhOX5JpX5KMhUgL.Foe4eh2pSo.7S0-2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoM01K5peKq4ehMf; SINAGLOBAL=8505429497315.529.1632922843183; ULV=1639136383200:2:1:1:3763013819565.094.1639136383093:1632922843184; ALF=1670672351; SCF=AoMImLiEPADgRCx1ffu6aj6AK92GFULp5oaCrYYu3UyFQ1CaK7GE8lZnOmRTsnXxymUaky46S2SrG5WmaKwfqDc.; SUB=_2A25Mt0wwDeRhGeVH61MQ9ifMzDmIHXVvxTr4rDV8PUNbmtAKLUGtkW9NT2jo5JhLkwNEFUwWQ_iTWmiOS-eqHHhv; SSOLoginState=1639136352; _s_tentry=www.baidu.com; Apache=3763013819565.094.1639136383093",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
}
# for name in stars:
#     time.sleep(1)
#     try:
#         if os.path.exists(name+'_sina.html'):
#             continue
#         # with open(name+'_sina.html','w') as f:
#         time.sleep(1)
#         r = requests.get(url = url+name,headers = headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         ret = str(r.text)
#         print(ret)
#         #f.write(ret)
#     except:
#         continue


for name in stars:
    time.sleep(1)
    try:
        if os.path.exists(name+'_sina.html'):
            print(name,"Success")
            continue
        with open(name+'_sina.html','w') as f:
            time.sleep(1)
            r = requests.get(url = url+name,headers = headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            ret = str(r.text)
            # print(ret)
            f.write(ret)
            print(name,"Success")
    except:
        print(name,"Failure")
        continue
