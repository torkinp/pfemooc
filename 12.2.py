import urllib
# from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    total = total + int(tag.contents[0])

print total
