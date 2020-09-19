num = 0
largest = -1
smallest = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        numb = float(num)
    except:
        print("Invalid input")

    if smallest is None:
        smallest = numb

    elif numb < smallest:
        smallest = numb

    elif numb > largest:
        largest = numb

print("Max Number is:", largest)
print("Min Number is:", smallest)
