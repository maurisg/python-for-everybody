import string

count = 0                       # Initialize variables
my_dictionary = {}
my_list = []

file = input("Enter file name: ")

try:
    file = open(file)

except FileNotFoundError:
    print("File cannot be opened:", file)
    exit()

for line in file.readlines():                               # Removes numbers and punctuation, divides words into list
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    words = line.split()

    for word in words:
        lowercase = word.lower()                            # Makes every word lowercase

        for letter in lowercase:
            count += 1                                      # Counts each letter for relative frequency

            if letter not in my_dictionary:
                my_dictionary[letter] = 1

            else:
                my_dictionary[letter] += 1

for letter, value in my_dictionary.items():                 # Transformation from dictionary into list of tuples
    my_tuple = value/count, letter
    my_list.append(my_tuple)

my_list = sorted(my_list, reverse=True)                     # Sorts list in descending order

print("RELATIVE FREQUENCY IN THE FILE")

for value, letter in my_list:
    print(letter, value)                                    # Prints letter first and then value.
