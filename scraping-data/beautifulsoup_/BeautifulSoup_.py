from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

fu = UserAgent()
header = {'user-agent':fu.chrome}
url = 'http://www.trustedavatar.com/'
request = requests.get(url,headers=header)
html = request.text
soup = BeautifulSoup(html,"lxml")

print (soup.prettify())
#print (soup.title)
#print (soup.get_text())
#print (soup.find_all()) # hyperlinks
#print (soup)