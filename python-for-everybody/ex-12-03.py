import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def findURL(url, pos) :
    print("Retrieving: ", url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    return tags[pos-1].get('href', None)


url = input('Enter URL: ')
count_str = input('Enter count: ')
count = int(count_str)
pos_str = input('Enter position: ')
pos = int(pos_str)

while count >= 0 :
    url = findURL(url, pos)
    count = count - 1
