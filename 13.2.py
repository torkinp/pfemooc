import json
import urllib

url = raw_input('Eneter Location: ')
uh = urllib.urlopen(url)
data = uh.read()
try: js = json.loads(data)
except: js = None
if 'note' not in js:
    print '==== Failure To Retrieve ===='
    print data
    quit()
    
total = 0

for c in js['comments']:
    total = total + c['count']

print total
