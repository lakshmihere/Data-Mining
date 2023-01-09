import requests

def find_director(url):
    
    response = requests.get(url)

    # Make sure that you got a valid response
    if(response.ok):
        # Get the full data from the response
        data = response.text
        #print(data)

    soup = BeautifulSoup(data, 'html.parser')
    infobox = soup.find(class_ = "infobox")
    labels = infobox.find_all(class_ = "infobox-label")
    for label in labels:
        if label.get_text()== "Directed by":
            data_dir = label.find_next(class_ = "infobox-data")
            return(data_dir.get_text())



url = "https://en.wikipedia.org/wiki/Tom_Cruise_filmography"
response = requests.get(url)

# Make sure that you got a valid response
if(response.ok):
  # Get the full data from the response
  data = response.text
  #print(data)

from bs4 import BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())


filmSpan = soup.find(id="Film")
#print(filmSpan.prettify())
h2 = filmSpan.parent
#print(h2.prettify())
tbl = h2.next_sibling.next_sibling
#print(tbl.prettify()[0:600])
count = 0
f = open("demofile.csv", "w")
f.write(f"title,role,director\n")
for tr in tbl.select("table tbody tr"):
    count = count + 1
    if count == 1:
        continue
    row_el = tr.find_all('td')
    
    a_lst = row_el[0].select("i a")
    if not a_lst:
        a_lst = row_el[0].select("span a")
    a = a_lst[0]
    url = a.get('href')
    title = a.get('title')
    role = row_el[1].get_text()
    director = find_director('https://en.wikipedia.org/'+url)
    role = role.strip()
    director = director.strip()
    details = [title, role, director]
    #print(details)
    f.write(f"{title},{role},{director}\n")
f.close()
    




