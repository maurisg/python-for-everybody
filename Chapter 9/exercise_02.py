my_dictionary = {}
file = input("Enter file name: ")

try:
    file = open(file)

except FileNotFoundError:
    print("File cannot be opened:", file)
    exit()

for line in file.readlines():
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue

    else:
        if words[2] not in my_dictionary:
            my_dictionary[words[2]] = 1

        else:
            my_dictionary[words[2]] += 1

print(my_dictionary)
