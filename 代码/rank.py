import os
import re
import json
import ast
filelist = os.listdir(os.getcwd())
for i in filelist:
    if re.match(r'.*_hm.txt',i) is None:
        filelist.remove(i)
        
total = []
for file in filelist:
    with open(file,"r") as f:
        for line in f.readlines():
            splited = line.split(",")
            str1 = "".join(','+splited[i] for i in range(1,len(splited)))
            ret = ast.literal_eval(str(str1[1:]).replace(" ","").replace('\n',''))
            ret.update({'name':splited[0]})
            print(ret)
            total.append(ret)
            
for i in sorted(total,key=lambda x:x['avg'],reverse=True)[:500]:
    print(i['name'])