import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
product_name=[]

names = soup.find_all("a",class_ = "title")
# print(names) # comment due to very long output
for i in names:
    p_name = i.text
    product_name.append(p_name)
# print(product_name)

prices = soup.find_all("h4",{"class":"pull-right","class":"price"})
prices_list = []

for i in prices:
    price = i.text
    prices_list.append(price)

# print(prices_list)

desc = soup.find_all("p",class_ = "description")
desc_list  = []

for i in desc:
    desc_name = i.text
    desc_list.append(desc_name)

# print(desc_list)


rev = soup.find_all("p",class_ = "review-count")
# print(rev) # comment
rev_list = []

for i in rev:
    rew = i.text
    rev_list.append(rew)

# print(rev_list)


df = pd.DataFrame({
    "Product Name":product_name,
    "Prices" : prices_list,
    "Description" : desc_list,
    "Reviews" : rev_list
                   })

df.to_csv("newDataFrame.csv",index=False)