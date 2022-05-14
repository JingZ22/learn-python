import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET


url = input('Enter location: ')
print('Retrieving', url)
uh = urlopen(url)
data = uh.read()
print('Retrieving', len(data), 'characters')
tree = ET.fromstring(data)

results = tree.findall('.//count')
print("count: ", len(results))
total = 0
for item in results :
    total = total + int(item.text)
print('sum:', total)
