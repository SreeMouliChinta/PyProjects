Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fname = input("Enter file:")
fhand = open(fname)
hours = dict()
words = list()
for line in fhand:
    line.rstrip()
    if line.startswith('From '):
        line = line.split()
        words.append(line[5].split(":"))
for word in words:
    hours[word[0]] = hours.get(word[0],0) + 1

lst = []

for a,b in hours.items():
    lst.append((a,b))

lst.sort()


for a,b in lst:
    print(a,b)
