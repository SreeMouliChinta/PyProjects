#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
#and summing up the integers.

fname = input('Enter file name: ')
fhand = open(fname)
list = list()

import re
for line in fhand :
    line = line.split()
    extract = re.findall('([0-9]+)',line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        list.append(num)

print(sum(list))
