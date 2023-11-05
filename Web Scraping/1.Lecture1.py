from bs4 import BeautifulSoup
import requests

url = ('https://webscraper.io/test-sites/e-commerce/allinone/computers')

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
print(soup)