fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
words = list()
d = dict()

for line in fh:
    words = line.split()
    if len(words) > 0:
        if 'From:' in words[0]: continue
        if 'From' in words[0]:
            email = words[1]
            d[email] = d.get(email,0) + 1

bigc = None
bige = None
for e,c in d.items():
    if bigc is None or c > bigc:
        bige = e
        bigc = c

print bige, bigc
