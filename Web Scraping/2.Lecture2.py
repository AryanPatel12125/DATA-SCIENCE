from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
# print(soup.div)


# tag = soup.header
# print(tag.attrs)
# atb = (tag.attrs)
# print(atb["role"])

# tag = soup.div.p
# print(tag.string)

tag = soup.header.div.a.button.span
print(tag.string)

# price = soup.find("h4", {"class":"pull-right"})
# print(price.string)

