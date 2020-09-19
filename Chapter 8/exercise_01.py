my_list = []        # Creates an empty list

try:
    n = int(input("Enter the number of elements in the list: "))
    for i in range(0, n):
        element = (input())
        my_list.append(element)

except:
    print("Invalid input. Please enter a number.")
    exit()


def chop(lst):
    del lst[0]      # Deletes first element of the list
    del lst[-1]     # Deletes last element of the list


def middle(lst):
    new = lst[:]    # Stores all elements of previous list
    return new


chop_list = chop(my_list)
print(chop_list)

middle_list = middle(my_list)
print(middle_list)
