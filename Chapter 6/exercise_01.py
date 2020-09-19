index = 0
char = 0
entry = input("Please write a word or sentence: ")

while len(entry) > index:
    letter = entry[char - 1]
    print(letter)
    char = char - 1
    index = index + 1
