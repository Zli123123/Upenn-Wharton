import urllib 
from bs4 import BeautifulSoup


import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen

# providing url
url = "https://twitter.com/michaeljburry?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
#https://www.geeksforgeeks.org/how-to-automate-an-excel-sheet-in-python/?ref=feed
# opening the url for reading
html = urlopen(url)

# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')

# getting all the paragraphs
for para in htmlParse.find_all("p"):
    print(para.get_text())

text = para.get_text()

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