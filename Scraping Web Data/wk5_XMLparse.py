# import xml.etree.ElementTree as ET

# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''

# tree = ET.fromstring(data)
# print('Name: ', tree.find('name').text)
# print('Attr: ', tree.find('email').get('hide'))

url = 'http://py4e-data.dr-chuck.net/comments_1378886.xml'

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
#import ssl

# api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

count = 0
sum = 0


# url = input('Enter location: ')

# parms = dict()
# parms['address'] = address
# if api_key is not False: parms['key'] = api_key
# url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

# results = tree.findall('count')
# print(results)
# commentinfo = tree.findall('commentinfo/comments/comment/count')
# print(commentinfo)
# comments = tree.findall('comments')
# print(comments)
comment = tree.findall('comments/comment')
# print(comment)
# counts = tree.findall('count')
# # count = counts.
# print(counts)

for item in comment:
    # print(item)
    count += 1
    sum += int(item.find('count').text)
    


print("Sum: ",sum,"\nCount: ", count)