from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

file = open('complex.html')
data = file.read()
file.close()
soup = BeautifulSoup(data,'lxml')

# tag.contens  returns list of children

title = soup.title
parent = title.parent # very last parent
print (parent.name)

parents = soup.a.parents

for parent in parents:
    print (parent.name)




