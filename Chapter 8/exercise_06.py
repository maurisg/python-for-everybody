my_list = []
max_number = None
min_number = None

while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        numb = float(num)
        my_list.append(numb)
        max_number = max(my_list)
        min_number = min(my_list)

    except:
        print("Invalid input.")

print("Maximum:", max_number)
print("Minimum:", min_number)
