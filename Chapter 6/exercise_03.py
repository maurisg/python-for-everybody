def counter(word, letter):
    count = 0
    print("Word: " + word, "\nLetter: " + letter)
    for char in word:
        if char == letter:
            count = count + 1
    print("Number of", letter + ":", count)


counter("Banana", "a")
