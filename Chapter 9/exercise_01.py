my_dictionary = {}                                        # Creates an empty dictionary
count = 0
file = open("words.txt")

entry = input("Write the word you are searching for: ")   # Allows the user to search for the word inside the command line

for line in file.readlines():
    words = line.split()
    for word in words:
        count = count + 1
        if word in my_dictionary:
            continue
        my_dictionary[word] = count

if entry in my_dictionary:
    print('True')

else:
    print('False')
