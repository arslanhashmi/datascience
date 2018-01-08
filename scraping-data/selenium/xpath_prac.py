from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

chrome_driver = 'D:\softwares\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)
'''
driver.get('https://www.instagram.com')

sleep(5)
login_button = driver.find_element_by_xpath("//span[@id='react-root']//p[@class='_dyp7q']/a") # // whole descendants / direct child

login_button.click()

sleep(5)
'''
#google example

driver.get('https://www.google.com')
sleep(2)
search = driver.find_element_by_xpath("//input[@id='lst-ib']") # // whole descendants / direct child
search.send_keys('valid key expression')

search.submit()
sleep(5)




driver.close()


