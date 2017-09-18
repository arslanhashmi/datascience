from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import re

url = 'http://www.codingbat.com/java'
user_agent = UserAgent()
page = requests.get(url,headers={'user-agent':user_agent.chrome})
soup = BeautifulSoup(page.text,'lxml')

attr = {'class':'products'}
divs = soup.find_all('span',attrs=attr)

attr = {'class':'summ'}
divs = soup.find_all('div',attrs=attr)

base_url = 'http://www.codingbat.com'
topics_java = {div.a.span.string:base_url+div.a['href'] for div in divs}

with open ('links','w') as myFile:
    for key,value in topics_java.items():
        #print (key," ",value)
        #myFile.write(key+" "+value+"\n")
        pass
with open ('question.txt','w') as question:
    for key,value in topics_java.items():
        second_page = requests.get(value, headers={'user-agent': user_agent.chrome})
        second_soup = BeautifulSoup(second_page.text, 'lxml')
        attr = {'class': 'tabc'}
        divs = second_soup.find('div', attrs=attr)
        #print (divs)
        #question.write('Questions for '+ key+"\n")
        print('Questions for '+ key)
        i = 1
        for td in divs.table.find_all('td'):

            third_page = requests.get(base_url+td.a['href'], headers={'user-agent': user_agent.chrome})
            third_soup = BeautifulSoup(third_page.text, 'lxml')
            attr = {'class': 'minh'}
            divs = third_soup.find('div', attrs=attr)
            title = third_soup.find('div',attrs={'class':'indent'})

            print ("Question # "+str(i),title.find_all('span')[1].string,divs.string)
            #question.write ("Question # ")
            #question.write (str(i))

            #question.write (str(title.find_all('span')[1].string) if is not None else '' +" "+divs.string+"\n")

            i+=1


