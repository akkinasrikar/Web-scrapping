from bs4 import BeautifulSoup
import requests

url = 'https://www.freetutorialshub.com/web-scraping-with-python-beautifulsoup-requests-selenium/'

response=requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')

tags= soup.find_all('a')

for tag in tags:
	print(tag.get('href'))
