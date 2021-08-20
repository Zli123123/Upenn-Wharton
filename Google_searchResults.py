from googlesearch import search   
import Help

# to search 
query = "nvidia news"

links = []
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    links.append(j) 

print(links)

Help.scrape(links)