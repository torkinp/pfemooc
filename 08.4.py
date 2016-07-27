fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
longlst = list()
for line in fh:
    lst = line.rstrip().split()
    for word in lst:
        if word not in longlst: longlst.append(word)

longlst.sort()
print longlst

