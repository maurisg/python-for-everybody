# The file and the code have to share the same folder, otherwise it will display an error.

file_name = input("Enter a file name: ")
open_file = open(file_name)

for line in open_file.readlines():
    print(line.upper().strip())
