
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import re

file = open('complex.html')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')

#print (soup.find_all('div'))

regex = re.compile('^div')

for tag in soup.find_all(regex):
    #print (tag.name)
    pass

for tag in soup.find_all(['a','b']):
    #print (tag.name)
    pass

def has_name(tag):
    return (tag.has_attr('name')) #should return true or false

for tag in soup.find_all(has_name):
    #print (tag.name)
    pass

#by attributes

attr = {'class':'three','name':'three'}
#print (soup.find_all('div',attrs=attr))

#print (soup.find_all('div',limit=1))

regex = re.compile('This')
print (soup.find_all(string=regex))

for tag in soup.find_all(class_='three'):
    print (tag.name)

for tag in soup.find_all(class_=re.compile('t')):
    print (tag.name)


# recursive parameter only let the soup to find the very first children

print (soup.find_all('title',recursive=False))
print (soup.find_all('title',recursive=True))
