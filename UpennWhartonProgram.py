import nltk
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
import re

driver = webdriver.Chrome()
driver.get('https://seekingalpha.com/article/4448637-amd-intel-nvidia-best-chip-stock')
htmlSource = driver.page_source
#print(htmlSource)

soup = BeautifulSoup(htmlSource, 'html.parser')
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()


#print(visible_text)


#text = "I love good ham. I love poor and profitable sam."

a_list = nltk.tokenize.sent_tokenize(visible_text)

#print(a_list)
#print("___________________")

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

#print("new alist, ", a_list)

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

print("_________________________________")
for i in range(len(a_list)):
    if len(re.findall(r"(\+*|\-*)(\d+\.*\d*\%)", a_list[i])) != 0:
        print(a_list[i])
        