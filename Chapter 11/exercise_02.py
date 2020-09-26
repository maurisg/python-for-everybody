import re

count = 0
total = 0
file = open("mbox-short.txt")

for line in file:
    line = line.rstrip()
    number_extraction = re.findall('New Revision: ([0-9.]+)', line)

    for number in number_extraction:
        value = int(number)
        total = total + value
        count += 1

average = total / count
print("Average:", int(average))
