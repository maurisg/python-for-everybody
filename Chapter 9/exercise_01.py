index = 0
variable = 0
entry = input("Please write a word or sentence: ")

while len(entry) > index:
    letter = entry[variable - 1]
    print(letter)
    variable = variable - 1
    index = index + 1
