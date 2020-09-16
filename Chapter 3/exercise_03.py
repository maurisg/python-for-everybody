grade = input("Enter grade [0.0 - 1.0]: ")

try:
    grade = float(grade)
    if 0 <= grade <= 1.0:
        if grade >= 0.9:
            print("Your grade: A")

        elif 0.8 <= grade < 0.9:
            print("Your grade: B")

        elif 0.7 <= grade < 0.8:
            print("Your grade: C")

        elif 0.6 <= grade < 0.7:
            print("Your grade: D")

        else:
            print("Your grade: F")

    else:
        print("Please enter a valid grade.")

except:
    print("Please enter a valid grade.")
