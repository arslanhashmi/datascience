from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import re

file = open('consumer_report.txt')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')

attr = {'class':'products'}
divs = soup.find_all('span',attrs=attr)

for div in divs:
    #print (div.string)
    pass

# or

attr = {'class':'entry-letter'}
divs = soup.find_all('div',attrs=attr)

for div in divs:
    #print (div.div.a.span.string)
    pass

list = [div.div.a.span.string for div in divs]
for item in list:
    #print (item)
    pass


links = [div.div.a['href'] for div in divs]
for item,link in zip(list,links):
    #print (item," ",link)
    pass

# or

products = {div.div.a.span.string:div.div.a['href'] for div in divs}
for key,value in products.items():
    print (key," ",value)