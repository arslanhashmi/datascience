from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

file = open('sample.html')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')
print (soup.div.string) #string in the tag
print (soup.div.p.string) #string in the tag
soup.div.p.string.replace_with("paragraph's string has been changed")
print (soup.div.p.string)






