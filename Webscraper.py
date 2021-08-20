import nltk
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://www.fool.com/investing/2021/07/29/will-nvidia-be-a-trillion-dollar-stock-by-2025/').read()
#print(text_from_html(html))

text = (text_from_html(html))


a_list = nltk.tokenize.sent_tokenize(text)

#print(a_list)
print("___________________")

#cleanse of periods and that bad stuff

for i in range(len(a_list)):
    line = a_list[i]
    #print(line)
    newline = ""
    for char in line: 
        if char not in ".?\|/!-":
            newline = newline + char
    a_list[i] = newline
    newline = ""

print("new alist, ", a_list)
print("_________")
print("____________")
print("________________")

goodstuff = ["good", "soar", "increase", "up", "profitable"]

badstuff = ["poor", "bad", "decrease", "plummet", "debt"]

print("")

for i in range(len(a_list)):
    textlol = a_list[i]
    words = textlol.split()
    for k in range(len(words)):
        for nice in goodstuff:
            if words[k] == nice:
                print("#######################")
                print(a_list[i])
        for bad in badstuff: 
            if words[k] == bad:
                print(a_list[i])