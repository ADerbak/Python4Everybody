# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')



url_list = []
url_list.append(url)
#print(url_list[0])
count = int(input('Enter count: '))
position = int(input('Enter position: '))
#name = re.findall(r'.*known_by_([a-zA-Z]+).html', str(current_url))

for i in range(0,count):
    url_temp = []
    url_temp.append(url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print(tags)
    for tag in tags:
        urls = tag.get('href', None)
        url_temp.append(urls)
    url_list.append(url_temp[position])
    #print(url_list)
    url = url_temp[position]
    

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

#print(url_list)

name = []

for i in url_list:
    name_temp = re.findall(r'.*known_by_([a-zA-Z]+).html', str(i))
    name_temp = ''.join(name_temp)
    #print(name_temp)
    name.append(str(name_temp))

print(' '.join([a for a in name]))
print(name[-1])