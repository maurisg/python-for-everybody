def computepay():
    hours = input("Enter Hours: ")
    rate = input("Enter Rate: ")

    try:
        if float(hours) > 40:
            pay = float(hours) * float(rate)
            overtime = (float(hours) - 40) * (float(rate)*0.5)
            pay = pay + overtime
            print("$" + str(pay))

        else:
            pay = float(hours) * float(rate)
            print("$" + str(pay))

    except:
        print("Please enter a number.")


computepay()
