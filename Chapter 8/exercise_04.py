my_list = []

try:
    file_name = input("Enter a file name: ")    # Enter romeo.txt
    open_file = open(file_name)

    for line in open_file.readlines():
        words = line.split()
        for word in words:                     
            if word not in my_list:             
                my_list.append(word)
            else:
                continue

except:
    print("Invalid file name.")
    exit()

my_list.sort()
print(my_list)
