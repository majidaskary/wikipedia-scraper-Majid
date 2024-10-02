#Wikipedia Scraper
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Shapur_II'

r = requests.get(url)

print('status code: ', r.status_code)
print('Type: \n', type(r.text))
print('Text: \n', r.text[:200])
