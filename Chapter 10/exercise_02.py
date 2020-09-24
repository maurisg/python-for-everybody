my_dictionary = {}                                      # Creates an empty dictionary
my_list = []                                            # Creates an empty list

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
        colon_position = words[5].find(":")             # Finds the position of the colon in the 5 index
        hour = (words[5][:colon_position])              # Stores the values of the first two positions in HH:MM:SS

        if hour not in my_dictionary:
            my_dictionary[hour] = 1                     # If the hour is not in dictionary then the value is 1

        else:
            my_dictionary[hour] += 1                    # If the value is in the dictionary, it adds 1

for key, val in my_dictionary.items():
    my_tuple = key, val                                 # Converts dictionary into tuple
    my_list.append(my_tuple)                            # Converts tuple into list [('a':1), ('b':2)...]

my_list = sorted(my_list)                               # Sorts list from lowest to highest value

for key, val in my_list:
    print(key, val)                                     # Prints hours and number of repeated hours, in ascending order.
