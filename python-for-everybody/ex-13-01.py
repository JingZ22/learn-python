import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json

url = input('Enter location :')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieving', len(data), 'characters')

js = json.loads(data)
#print(js)
dic = js['comments']
total = 0
for item in dic :
    total = total + int(item['count'])
print('count: ', len(dic))
print('sum: ', total)
