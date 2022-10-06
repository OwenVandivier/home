from bs4 import BeautifulSoup
import requests

# Set URL and create response
nfl_url = "https://www.espn.com/nfl/scoreboard"
response = requests.get(nfl_url)

# Constructor of URL response (raw HTML)
page = BeautifulSoup(response.content, 'html.parser')
print(page.body)



#print(page.prettify())

