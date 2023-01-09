import requests
url = 'https://bestlifeonline.com/funny-clean-jokes/'
response = requests.get(url)

# Make sure that you got a valid response
if(response.ok):
  # Get the full data from the response
  data = response.text
  #print(data)

  from bs4 import BeautifulSoup

soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())

# Make a list of all `<ol>` elements.
# Note that Beautiful Soup uses the syntax 'ol'
# to search for HTML `<ol>` elements.
soup.find_all('ol')
# Get the list
list = soup.find('ol')
items = list.find_all('li')
#print(items)

# Get the list
list = soup.find('ol')
items = list.find_all('li')
#print(items)
jokes = [joke.get_text() for joke in items]
#print(jokes)

# This gets a list of all `<div>` HTML elements on the page
soup.find_all('div')

# Get just the `<div>` elements with class 'content'
div = soup.find('div', class_='content')
list = div.find('ol')
items = list.find_all('li')
jokes = [joke.get_text() for joke in items]
#print(jokes)

# Get jokes in a sentence

count = 0
for count in range(0,len(jokes)):
    print(jokes[count])