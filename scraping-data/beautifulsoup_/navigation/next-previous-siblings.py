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


print (soup.div.next_sibling.next_sibling)
print (soup.span.previous_sibling.previous_sibling)

for sibling in soup.div.next_siblings:
    print (sibling.name)



