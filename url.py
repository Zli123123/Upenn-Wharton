

import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
    
with urlopen("http://www.python.org") as url:
    s = url.read()
    
print(s)

import html2text
from bs4 import BeautifulSoup

#soup = BeautifulSoup(urlopen('https://www.google.com/').read())

f = urlopen('https://investorplace.com/2021/06/upcoming-nvda-stock-split-sets-the-stage-for-buyers/') 
soup = BeautifulSoup(f.parse)





#txt = soup.find('div', {'class' : 'body'})

#print(html2text.html2text(txt))