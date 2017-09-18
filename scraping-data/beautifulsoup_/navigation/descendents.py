from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

file = open('complex.html')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')

# tag.contens  returns list of children

body = soup.body.descendants

for index,child in enumerate(body):
    print (index,child)




