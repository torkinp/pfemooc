import re

total = 0
fhand = open('regex_sum_298037.txt')
for line in fhand:
    line = line.rstrip()
    emnos = re.findall('[0-9]+', line)
    for num in emnos:
        total = total + int(num)

print total

