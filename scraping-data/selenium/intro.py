from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

chrome_driver = 'D:\softwares\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)
'''
driver.get('https://www.instagram.com')
soup = BeautifulSoup(driver.page_source,'lxml')
#print(soup.prettify())

sleep(5)
login_button = driver.find_element_by_link_text('Log in') # text of a link ('a') tag
login_button.click()

sleep(5)
'''
driver.get('https://www.google.com')
search = driver.find_element_by_id('lst-ib')
search.send_keys('valid key expression')

search.submit()
sleep(5)









driver.close()