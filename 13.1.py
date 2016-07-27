import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter url: ')

uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
total = 0
for c in counts:
     total = total + int( c.find('count').text)

print total

