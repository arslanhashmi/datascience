import requests

url = 'https://www.wikipedia.org/'
response = requests.get(url)
text = response.text
#text = response.content  #not indented
print (response.status_code)
print (response)
#print (text)

for key,value in response.headers.items():
    print (key," ",value)