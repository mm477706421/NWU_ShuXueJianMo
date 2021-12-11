import os
import requests
from bs4 import BeautifulSoup
import json
import gzip
from io import StringIO

url = "https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start=0"
headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Cookie': 'bid=4xZ2u3KMtGU; douban-fav-remind=1; __gads=ID=f7d127c88d41297f-22b70fab65cf00e8:T=1639144036:RT=1639144036:S=ALNI_MbXAMx-7C-c4xmPppl8PAJ-S7EkAw; __utma=30149280.1508031002.1639144038.1639144038.1639215545.2; __utmc=30149280; __utmz=30149280.1639215545.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118371"; __utmb=30149280.6.9.1639215591100; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1639215601%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKI-NHtDh7lnrjJn510Ih0boKKoosGBs0s2z5pLDCMqZ-a_DC-SVNbGhqFQvtvugd%26wd%3D%26eqid%3Daf4fdce7000a6c2e0000000661b471ee%22%5D; _pk_id.100001.4cf6=a1e5e5d2e946b2c9.1639215601.1.1639216715.1639215601.; _pk_ses.100001.4cf6=*; __utma=223695111.196932377.1639215601.1639215601.1639215601.1; __utmb=223695111.0.10.1639215601; __utmc=223695111; __utmz=223695111.1639215601.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D23CF14A0DAE3CD1CB602804E0050A043|af985a5b0c07bce70f32cdc545a6ed72',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Cache-Control': 'max-age=0',
}

if not os.path.exists(os.path.join(os.getcwd(),'douban')):
    os.makedirs('douban')
    print("Dir has been created")
else:
    print("Dir has already existed!")

DEBUG = 1
if not DEBUG:
    path = os.path.join(os.getcwd(),'douban')
    print("Working Path:"+path)
    with requests.Session() as s:
        with open("douban.html","w") as f:
            raw_dt = s.get(url=url)
            raw_dt.encoding = raw_dt.apparent_encoding
            bsdt = BeautifulSoup(raw_dt.text,"html.parser",from_encoding=raw_dt.apparent_encoding)
            f.write(raw_dt.text)
            for i in bsdt:
                print(i)
            
            
with open('douban.json',"r") as f:
    dt = json.loads(f.read())
    for i in dt['subjects']:
        print(i['title']+" "+i['url'])
        url = i['url']
        response = requests.get(url = url,headers=headers)
        bsdt = BeautifulSoup(response.text,"html.parser",from_encoding=response.apparent_encoding)
        