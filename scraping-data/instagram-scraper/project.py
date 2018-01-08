from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import os,requests,shutil

class App:
     def __init__(self,username='m.arslanijaz99@hotmail.com',password='noways12',target_username='awais.hashmii',path='instagram_scraping'):
         self.username=username
         self.password=password
         self.target_username=target_username
         self.path=path
         self.driver_path='/Users/arslan/Downloads/chromedriver'
         self.driver = webdriver.Chrome()
         self.driver.get('https://www.instagram.com')
         sleep(1)
         self.login()
         self.target()
         sleep(5)
         self.driver.close()

     def login (self):
         login_button = self.driver.find_element_by_link_text('Log in')  # text of a link ('a') tag
         login_button.click()
         sleep(1)
         username_field = self.driver.find_element_by_xpath('//input[@placeholder="Phone number, username, or email"]')
         username_field.send_keys(self.username)
         password_field = self.driver.find_element_by_xpath('//input[@placeholder="Password"]')
         password_field.send_keys(self.password)
         password_field.submit()
         sleep(2)


     def target(self):
         search_field = self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
         search_field.send_keys(self.target_username)
         sleep(1)
         self.driver.get(self.driver.current_url + self.target_username+'/')
         sleep(1)
         self.scroll_down()

     def scroll_down(self):
         try:
            total_posts = self.driver.find_element_by_xpath("//span[@class='_he56w']").text
         except Exception as e:
             print(e)
         #total_posts=int(str(total_posts.split(',')))
         #total_posts= total_posts.split(',')[0]+total_posts.split(',')[1]
         if int(total_posts)>12:
             self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
             sleep(1)
             load_more = self.driver.find_element_by_link_text('Load more')
             load_more.click()
             for i in range(int((int(total_posts)/12))):
                 sleep(0.1)
                 self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
             sleep(1)
         self.download_image()

     def download_image(self):
         soup = BeautifulSoup(self.driver.page_source,'lxml')
         images = soup.find_all('img',src=True)
         image_links = [image.get('src') for image in images]
         if not os.path.exists(os.path.join(self.path, 'captions')):
             os.makedirs(os.path.join(self.path, 'captions'))


         i = 1
         for link,image in zip(image_links,images):
             caption = image.get('alt')
             print (caption)
             file_name = str(link).split('/')[-1].split('?')[0]
             print ("Downloading Image:",i)
             i+=1
             path = os.path.join(self.path,file_name)
             response = requests.get(link,stream=True)
             sleep(0.5)
             with open (path,'wb') as image:
                 shutil.copyfileobj(response.raw,image)
             with open (os.path.join(self.path+'/captions',file_name+'.txt'),'w')as file:
                 try:
                    file.write('The image is : '+str(file_name)+'\nCaption is'+str(caption))
                 except Exception:
                    file.write('The image is : ' + str(file_name) + '\nCaption is having illegal data'  )

if __name__ == '__main__':
    app = App()


