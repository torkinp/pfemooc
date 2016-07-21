# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "File could not be opened: " + fname
    quit()

for line in fh:
    print line.rstrip().upper()

