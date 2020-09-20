file = open("mbox-short.txt")
count = 0

for line in file:
    if line.startswith('From:'):
        continue

    elif line.startswith("From"):
        words = line.split()
        print(words[1])

    else:
        continue

    count = count + 1

print("There were", count, "lines in the file with From as the first word")
