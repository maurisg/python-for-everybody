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
        at_position = words[1].find("@")            # Position of '@'
        domain_name = words[1][at_position+1:]      # Stores domain name after '@'

        if words[1] not in my_dictionary:
            my_dictionary[domain_name] = 1          # First entry

        else:
            my_dictionary[domain_name] += 1         # More counts

print(my_dictionary)
