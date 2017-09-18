from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

file = open('sample.html')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')

print (soup.meta.get('charset'))  # or mera['charset']
soup.body['style']='some style'
print (soup.body['style'])
print (soup.body['class'])
print (soup.div)
