import requests
from bs4 import BeautifulSoup

url = 'https://twitter.com/michaeljburry?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

print("")

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

print(output)

text = output

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

goodstuff = ["good", "soar", "increase", "up", "profitable", "southern"]

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