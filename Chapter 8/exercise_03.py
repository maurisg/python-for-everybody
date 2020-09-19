file = open("mbox-short.txt")
count = 0

for line in file:
    words = line.split()

    if len(words) == 0 or words[0] != "From":
        continue

    print(words[2])
