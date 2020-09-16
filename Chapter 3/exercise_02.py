hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    if float(hours) > 40:
        pay = float(hours) * float(rate)
        overtime = (float(hours) - 40) * (float(rate)*0.5)
        pay = pay + overtime
        print(pay)

    else:
        pay = float(hours) * float(rate)
        print(pay)

except:
    print("Please enter a number.")
