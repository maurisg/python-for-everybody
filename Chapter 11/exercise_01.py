import re

count = 0
file = open("mbox-short.txt")
expression = input("Enter a regular expression: ")

for line in file:
    line = line.rstrip()
    x = re.findall(expression, line)
    if len(x) > 0:
        count += 1

print("\'mbox-short.txt\' had", count, "lines that matched:", expression)
