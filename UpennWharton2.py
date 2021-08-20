import nltk
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests


res = requests.get('https://seekingalpha.com/article/4448637-amd-intel-nvidia-best-chip-stock')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
linkElems = soup.select('p')
html = []
for i in range(len(linkElems)):
    html.append(linkElems[i].getText())
text = ' '.join(html)
print(html)


#text = "I love good ham. I love poor and profitable sam."

a_list = nltk.tokenize.sent_tokenize(text)

print(a_list)
print("___________________")

#cleanse of periods and that bad stuff

for i in range(len(a_list)):
    line = a_list[i]
    print(line)
    newline = ""
    for char in line: 
        if char not in ".?\|/!-":
            newline = newline + char
    a_list[i] = newline
    newline = ""

print("new alist, ", a_list)

goodstuff = ["save", "soar", "increase", "up", "profitable", "southern"]

badstuff = ["poor", "bad", "decrease", "plummet", "debt"]

print("")

for i in range(len(a_list)):
    textlol = a_list[i]
    words = textlol.split()
    for k in range(len(words)):
        for nice in goodstuff:
            if words[k] == nice:
                print(a_list[i])
        for bad in badstuff: 
            if words[k] == bad:
                print(a_list[i])