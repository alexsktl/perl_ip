import requests
import re
from bs4 import BeautifulSoup
import time
dic=set()
end=time.clock()+24*3600
while time.clock()<end:
    try:
        h=requests.get('https://news.yahoo.com/politics/')
        soup = BeautifulSoup(h.content, 'html.parser')
        soup.find_all(text='"type": "article"')
        for a in soup.find_all('a', href=True):
            if re.search('democr',a['href'])!= None or re.search('republ',a['href'])!= None:
                if a['href']not in dic:
                    dic.add(a['href'])
                    f = open('log.txt', 'a')
                    f.write('https://news.yahoo.com/politics'+a['href']+'\n')
                    f.close()

    except:
        pass
    time.sleep(600)