import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_1378887.json'

uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

info = json.loads(data)
print('User count:', len(info))

# print('Count', info['comments'][3]['count'])

count = 0
sum = 0

for i in range(0,len(info['comments'])):
    #print('Count', info['comments'][i]['count'])
    count += 1
    sum += int(info['comments'][i]['count'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])


print("Count of Records:",count)
print("Sum of Records:",sum)