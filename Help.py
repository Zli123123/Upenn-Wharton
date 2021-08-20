from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from bs4 import BeautifulSoup
import nltk
import re

def scrape(links):
    for z in range(len(links)):
        driver = webdriver.Chrome()
        driver.get(links[z])
        htmlSource = driver.page_source
        #print(htmlSource)
        
        soup = BeautifulSoup(htmlSource, 'html.parser')
        #print(soup)
        #print(soup.select('p'))
        elems = soup.select('p')
        text = []
        for i in range(len(elems)):
            text.append(elems[i].getText())
        #print(text)
        #print(visible_text)
        text = " ".join(text)
        
        a_list = nltk.tokenize.sent_tokenize(text)
        
        #print(a_list)
        #print("___________________")
        
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
        
        #print("new alist, ", a_list)
        
        goodstuff = ["save", "soar", "increase", "up", "profitable", "southern", "growth"]
        
        badstuff = ["poor", "bad", "decrease", "plummet", "debt"]
        
        #print("_______________________________________________________________")
        
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