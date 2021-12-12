from bs4 import BeautifulSoup
import os
import re

list_file = os.listdir(os.getcwd())
for file_name in list_file:
    if re.match(r'.*._sina.html',file_name) is None:
        list_file.remove(file_name)
total_fans_cnt = open("total_fans_cnt.txt","a+")
total_fans_cnt.seek(0,0)
for file in list_file:
    try:
        with open(file,"r") as f:
            name = file.split('_')[0]
            bsdt = BeautifulSoup(f.read(),"html.parser",from_encoding="utf-8")
            if bsdt.find("span",attrs={'class':'s-nobr'}) is not None:
                print(name+" "+str(bsdt.find("span",attrs={'class':'s-nobr'}).contents[0]))
                total_fans_cnt.write(name+" "+str(bsdt.find("span",attrs={'class':'s-nobr'}).contents[0])+'\n')
    except:
        continue
print(list_file)