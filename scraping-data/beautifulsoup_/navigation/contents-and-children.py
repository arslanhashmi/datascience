from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

file = open('complex.html')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')

# tag.contens  returns list of children but only direct children

body = soup.body
for child in body.contents:
    print (child if child is not None else '',end="\n<-------->\n")


# .children  returns an iterator

for child in body.children:
    print (child if child is not None else '',end="\n<-------->\n")






