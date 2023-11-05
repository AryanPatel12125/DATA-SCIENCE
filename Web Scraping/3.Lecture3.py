from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
# price = soup.find("h4",{"class":"price","class" : "pull-right"})

# print(price.string)

desc = soup.find("p",{"class":"description"})
print(desc.string)

print(soup.find("p",class_ = "description"))