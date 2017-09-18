import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}
page = requests.get("https://www.google.com",headers=header,timeout=3)
print (page.text)
# print (ua.chrome)

#time outs
