import requests
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers")

soup = BeautifulSoup(r.text,'lxml')

# boxes = soup.find_all("div",class_ = "col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))

# box = soup.find_all("div",class_ = "col-md-4 col-xl-4 col-lg-4")[3]
# print(box)

# name = box.find("a").text
# print(name)

# desc = box.find("p",class_ = 'description').text
# print(desc)

navbar = soup.find_all("ul",class_ = "nav",id_ = "side-menu")
text = navbar.find("li",class_="active") 
print(text.text)