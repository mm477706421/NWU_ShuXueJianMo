import requests
import time
import pandas as pd 
import numpy as np
import os
import json

name = "白雪"
url = r'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?word=[[{"name":"'+name+'","wordType":1}]]&area=0&days=30'
print(url)
headers = {
"Host": 'index.baidu.com',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://index.baidu.com/v2/main/index.html',
'Connection': 'keep-alive',
'Cookie': 'BAIDUID=6EE4B14CF0C5FFBD8BC51FE2BD5CC1A2:FG=1; BIDUPSID=6EE4B14CF0C5FFBDCDDAA3478440FB86; PSTM=1628165068; __yjs_duid=1_6bfdb0ac0e3760480bbcac4da6e828871628176157265; BDUSS=X5NT1F4RjA2UmN4WnBOaVNkdX5QOC1iM2Nad3kyMmEzVUFmMmgxM1AzRUw4Mk5oRVFBQUFBJCQAAAAAAAAAAAEAAACPk8sQt67U88jwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtmPGELZjxhV; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=35295_35104_31254_35435_35456_34584_34504_34606_35329_35315_26350; BDSFRCVID=hFtOJexroG04sxcH4wwF-tse4ec_23JTDYLEL5mveYl6oVFVJeC6EG0Ptq6Ex2P-EHtdogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbAOVCD2JKL3fP36q4OHht_tMq0X5-RLf273ah7F5l8-hCb6b-IKXUv3etoMeR3e5RnB3qrCBD3xOKQphUIhyjO-04FLBf0qbCJLLnbN3KJm8tP9bT3vLfuyjtcz2-biW5KH2MbdflbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6L3-RJH-xQ0KnLXKKOLVKDyWl7ketn4hUt2jbtb-PAJ-bbjH6ne0CbHKMAKhpc2QhrdQf4WWb3ebTJr32Qr-qcH0KQpsIJM5bL-QJvX02c4Bn3baKvia-I-BMb1bqbDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6oM-Uvy-40XKD600PK8Kb7VbnnD5MnkbJkXhPtjtnJOK2-JL-3IH4b5eDbN-pPKDUI7Qbrr0xAta6c-hR4KaMQPSlcNLTjpQT8r5hLq0RkHLPj4aPbeab3vOPI4XpO1ef0zBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqtJHKbDH_KPMtMK; ab_sr=1.0.1_Mjk1MjAzY2E5NTZkODAxY2NiNDQ5YmY4N2U5NzExOWNmZmQ0OWE3YTM4ZGUxMmI1MzNjMTYxMDIxMWQxZWU3NmU5MTFlYzc2NTQ0MmQzYjZmZDVjNzQwMzE5NjQ4Yjk2ZjFmMmI3NGJhMGQ4NTlmN2FiZmMyOWIwYzgxZTI0NjAwMjkyYTBlODA3ODU2NjNkN2QyNTRhMDc1M2E0M2FhMA==; BA_HECTOR=a021248020058524cd1gr6nok0r; delPer=0; PSINO=6; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1639145239; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1639145471; RT="z=1&dm=baidu.com&si=6rc7piqj5be&ss=kx0gr626&sl=d&tt=6o8&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5109"; __yjs_st=2_ZmE0MWQ4MjVkYmQwMzcyYWZlNGYzNDY0MGFlMGNlMTdiZTBmZDIyNzNhZTQyNWM0NWQ1OTRlZDE0MjFlNzhhMWU5OWUyZDdmZjE3MTgxNjBhOWY5YTNiMGQxYjIzYTU5ZDRmOWRhMTgyOWFkODFkOGMzOTQ0NTE5N2IxZGFmODY1YzUzM2NiZDUwOGE2YTVkMzQ5YzljMDk2Y2RkZmQwY2QwNDVhNTNmNmYyZWQ1Zjk4YWMzYTRiODM4NDAzMjNhNDdlZmUwMjE4N2M4YjY3Y2JkMzMzMjBlOWZhMDQ1Yzk0YmNmYzlkM2EwZWU3NjA0Zjg5YTgzNGMwZGQ2NWE3MmJkMzYxNGRiNjZlZDJiOGM2NGMwNzAwNzgxZWZlMzMzXzdfNDNkM2FjNmQ=; bdindexid=vo1c73ivop6an83hkaavraogl3',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'same-origin',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
}

dt = pd.read_excel('result.xlsx','Sheet1')
stars = set()
for names in dt['Starring']:
    if names is not np.nan:
        for name in str(names).replace('、',',').replace('，',',').split(','):
            stars.add(name)
total_file = open("summary_hm.txt","a+")
total_file.seek(0,0)         
for name in stars:
    time.sleep(1)
    try:
        if os.path.exists(name+'_hm.txt'):
            continue
        with open(name+'_hm.txt','w') as f:
            time.sleep(1)
            url = r'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?word=[[{"name":"'+name+'","wordType":1}]]&area=0&startDate=2021-11-10&endDate=2021-12-09'
            print(url)
            r = requests.get(url = url,headers = headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            ret = str(r.text)
            ret = json.loads(ret)
            print(name+','+str(dict(ret['data'])['index'][0]['generalRatio'])+'Success')
            f.write(name+','+str(dict(ret['data'])['index'][0]['generalRatio'])+'\n')
            total_file.write(name+','+str(dict(ret['data'])['index'][0]['generalRatio'])+'\n')
    except:
        print(name + "Failure")
        continue


# for name in stars:
#     time.sleep(1)
#     try:
#         if os.path.exists(name+'_hm.html'):
#             print(name,"Success")
#             continue
#         with open(name+'_hm.html','w') as f:
#             time.sleep(1)
#             url = r'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?word=[[{"name":"'+name+'","wordType":1}]]&area=0&days=30'
#             r = requests.get(url = url,headers = headers)
#             r.raise_for_status()
#             r.encoding = r.apparent_encoding
#             ret = str(r.text)
#             print(ret)
#             f.write(ret)
#             print(name,"Success")
#     except:
#         print(name,"Failure")
#         continue
