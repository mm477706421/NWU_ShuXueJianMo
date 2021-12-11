import os
import shutil
import re
from bs4 import BeautifulSoup

listdir = os.listdir(os.getcwd())
if not os.path.exists("hm"):
    if not os.path.isdir("hm"):
        os.makedirs(os.path.join(os.getcwd(),"hm"),mode=0o777)
        print("Success create the html folder")
    else:
        print("Warnning: Html dir is already existed!")
else:
    print("Warnning: Html is already existed!")

try:
    for name in listdir:
        if re.match(r'.*_hm.txt',name) is not None:
            shutil.move(name,"hm/")
            print (name + "-->" + os.getcwd()+"/hm/"+name,end="\n") 
    print("Move files successfully")
except:
    print("Already done!")
    pass

stars_bd_file_list = os.listdir("html")
for file in stars_bd_file_list:
    try:
        with open(os.path.join(os.getcwd(),"html",file),"r") as f:
            line = 0
            try:
                for i in f.readlines():
                    line+=1
            except:
                pass
            print("length:"+str(line))
            if line <= 10:
                f.close()
                os.remove(os.path.join(os.getcwd(),"html",file))
                continue
            bsdt = BeautifulSoup(f.read(),"html.parser",from_encoding='utf-8')
            try:
                for i in bsdt.find(attrs={"class":re.compile("hint_[a-zA-Z0-9]{0,9} c_font_[a-zA-Z0-9]{0,9}")}):
                    print(i)
            except:
                print(file)
                pass
    except:
        print("utf-8"+file)