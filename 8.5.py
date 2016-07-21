fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
words = list()

for line in fh:
    words = line.split()
    if len(words) > 0:
        if 'From:' in words[0]: continue
        if 'From' in words[0]:
            count = count + 1
            print words[1]

print "There were", count, "lines in the file with From as the first word"
