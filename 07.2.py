# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "Could not open file:", fname
    quit()

count = 0.0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.lstrip("X-DSPAM-Confidence:")
    val = float(line.strip())
    count = count + 1
    total = total + val

print "Average spam confidence:", (total/count)

