count = 0
max_value = None
min_value = 0

while True:
    entry = input("Enter a number: ")
    if entry == "done":
        break
    try:
        value = float(entry)
    except:
        print("Invalid input.")
        continue

    if max_value is None or value > max_value:
        max_value = value

    elif value < min_value:
        min_value = value

    count = count + 1
