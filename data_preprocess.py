import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

part = 2
if part == 1:
    dt1 = pd.read_excel("附件一-电视剧评估信息.xlsx",'Sheet1')
    dt2 = pd.read_excel("附件二-电视剧基本信息.xlsx",'Sheet1')

    writer = pd.ExcelWriter("result.xlsx")
    #print(dt1.merge(dt2,left_on='TV Drama',right_on='TV Drama'))
    dtret = dt1.merge(dt2,left_on='TV Drama',right_on='TV Drama')
    dtret.to_excel(writer,'Sheet1')
    writer.save()
    writer.close()
    classes = {}
    for i in dt1.groupby('Theme'):
        classes.update({i[0]:i[1]})
    print(str([i for i in classes.keys()]))
    cnt_drama = [0 for i in range(12)]
    cnt_drama_comments = [0 for i in range(12)]
    for i,j in zip(dtret.sort_values(by='Date of Issuance License')['Date of Issuance License'].reindex(),
                   dtret.sort_values(by='Date of Issuance License')['Number of Comments'].reindex()):
        cnt_drama[int(i.split("/")[1])-1]+=1
        cnt_drama_comments[int(i.split("/")[1])-1]+=j
    #print(dtret[dtret['Score'] == 0])
    month = [i for i in range(1,13)]
    plt.bar(month,cnt_drama)
    plt.show()

dt = pd.read_excel('result.xlsx','Sheet1')
comment_max = dt['Number of Comments'].max()
Score_max = dt['Score'].max()
Episode_max = dt['Episode'].max()
Info_total = []
for i in dt.index:
    Info_new = []
    for j in dt.columns:
        if j == 'TV Drama':
            Info_new.append(dt[j][i])
        if j == 'Score':
            try:
                a = float(dt[j][i])
            except:
                a = 0
            Info_new.append(a)
        elif j == 'Number of Comments':
            try:
                a = float(dt[j][i]/comment_max)
            except:
                a = 0
            Info_new.append(dt[j][i])
            Info_new.append(a)
        elif j == 'Episode':
            try:
                a = float(dt[j][i]/Episode_max)
            except:
                a = 0
            Info_new.append(dt[j][i])
            Info_new.append(a)
    Info_total.append(Info_new)
for i in Info_total:
    Rscore = i[1]*i[2] - 0.2 * i[3]
    i.append(Rscore)

Info_dt = pd.DataFrame(Info_total)
Info_dt.columns = ['TV Drama','Score','Number of Comments','Chs','Episode','Ehs','RScore']
print(Info_dt.sort_values(by='RScore',ascending=False).head(10))
