import requests
from bs4 import BeautifulSoup

def find_director(url, title):
    print(f"{title} : {url}")

page = requests.get("https://en.wikipedia.org/wiki/Tom_Cruise_filmography")

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
filmSpan = soup.find(id="Film")
#print(filmSpan.prettify())
h2 = filmSpan.parent
#print(h2.prettify())
tbl = h2.next_sibling.next_sibling
#print(tbl.prettify()[0:500])
for a in tbl.select("table tbody tr td i a"):
    #print(a.prettify())
    url = a.get('href')
    title = a.get('title')
    find_director(url, title)