fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
words = list()
sw = list()
d = dict()

for line in fh:
    words = line.split()
    if len(words) > 0:
        if 'From:' in words[0]: continue
        if 'From' in words[0]:
            sw = words[5].split(':')
            hr = sw[0]
            d[hr] = d.get(hr,0) + 1

s = sorted(d.items())

for key,val in s:
    print key,val
