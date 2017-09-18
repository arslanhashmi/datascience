from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


file_name = 'consumer_report.txt'
url = 'http://www.consumerreports.org/cro/a-to-z-index/products/index.htm'
user_agent = UserAgent()
page = requests.get(url,headers={'user-agent':user_agent.chrome})
with open (file_name,'w') as file:
    file.write(page.content.decode('utf-8') if type(page.content) == bytes else file.write (page.content))

