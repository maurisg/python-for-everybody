hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)

if float(hours) > 40:
    overtime = (float(hours) - 40) * (float(rate)*0.5)
    pay = pay + overtime

else:
    print(pay)

print(pay)
