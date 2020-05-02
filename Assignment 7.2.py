#Write a program that prompts for a file name,
#then opens that file and reads through the file,
#looking for lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#(https://www.py4e.com/code3/mbox-short.txt)


fname = input('Enter file name:')
fhand = open(fname)
count = 0
num = 0
for line in fhand :
    if line.startswith('X-DSPAM-Confidence:') :
        line = line.rstrip()
        fline = line.find(' ')
        hline = line[fline+1 :]
        cline = float(hline)
        count = count + cline
        num = num+1
print('Average spam confidence:',count/num)
