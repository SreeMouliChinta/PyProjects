#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
#and summing up the integers.

fname = input('Enter file name: ')
fhand = open(fname)
list = list()
sum = 0

import re
for line in fhand :
    extract = re.findall('([0-9]+)',line)
    for num in extract :
        sum = sum + float(num)

print(int(sum))
