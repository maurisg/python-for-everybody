my_dictionary = {}                        # Creates an empty dictionary
file = input("Enter file name: ")
maximum = 0
maximum_address = ""

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
        if words[1] not in my_dictionary:
            my_dictionary[words[1]] = 1

        else:
            my_dictionary[words[1]] += 1

for key in my_dictionary:
    if my_dictionary[key] > maximum:        # my_dictionary[key] looks up the value of that key. 
        maximum = my_dictionary[key]
        maximum_address = key

print(maximum_address, maximum)
