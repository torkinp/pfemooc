import urllib
# from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter url: ')
count = int(raw_input('How many to count? '))
pos = int(raw_input('At what position? ')) - 1

for x in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Look at the parts of the tag
    url = tags[pos].get('href', None)
    print 'Contents:',tags[pos].contents[0]

