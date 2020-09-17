count = 0
total = 0

while True:
    entry = input("Enter a number: ")
    if entry == "done":
        break

    try:
        value = float(entry)


    except:
        print("Invalid input.")
        continue

    total = total + value
    count = count + 1

print(total, count, total/count)
