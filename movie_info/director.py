import requests
url = "https://en.wikipedia.org/wiki/Knight_and_Day"
response = requests.get(url)

# Make sure that you got a valid response
if(response.ok):
  # Get the full data from the response
  data = response.text
  #print(data)

from bs4 import BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())


infobox = soup.find(class_ = "infobox")
#print(infobox.prettify())
labels = infobox.find_all(class_ = "infobox-label")
for label in labels:
    if label.get_text()== "Directed by":
        data_dir = label.find_next(class_ = "infobox-data")
        print(data_dir.get_text())