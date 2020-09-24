my_dictionary = {}                                # Creates an empty dictionary
my_list = []                                      # Creates an empty list
  
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

for email, count in my_dictionary.items():        # Makes a list of tuples
    my_tuple = (count, email)
    my_list.append(my_tuple)

my_list = sorted(my_list, reverse=True)           # The list is sorted from largest to smallest

for count, email in my_list[:1]:                  # Prints the first one (largest)
    print(email, count)
