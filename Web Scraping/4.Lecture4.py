import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

prices = (soup.find_all('h4',class_='pull-right'))
print(len(prices))

# for i in prices:
#     print(i.text)

desc = soup.find_all("p",class_ = "description")

print(prices[3])
print(desc[3])

