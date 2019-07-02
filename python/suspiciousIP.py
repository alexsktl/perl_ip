import re
import pandas as pd
data=[]
with open ("access.log", "r") as myfile:
    for line in myfile:
        data.append(list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))))
df = pd.DataFrame(data)
df=df.drop(columns=[1,2,6,7])
df.columns=['Ip','Time','Type','Rcode','Com']
wl=['109.171.82.22']
bl=['92.94.108.47']
#Условия подозрительности:
#Список белых Ip
#Список черных Ip
#код 499
#кто пытался подключиться к php my admin кроме 109.171.82.22
#кто пытался подключиться к wp-login кромe 109.171.82.22
def susp(r):
    k=0
    if r['Rcode']==499:
        k+=1
    if r['Ip']not in wl:
        k+=1
    if r['Ip']in bl:
        k+=1
    a = re.search(r'wp-login*', r['Type'])
    if a is not None:
        if r['Ip']not in wl:
            k+=1
    a = re.search(r'phpmyadmin*', r['Type'])
    if a is not None:
        if r['Ip']not in wl:
            k+=1
    if k >= 2:
        return True
    else:
        return False
df['susp'] = df.apply(lambda x: susp(x), axis=1)
susp_zapr = df[df["susp"] == True]
print(susp_zapr['Ip'].unique())