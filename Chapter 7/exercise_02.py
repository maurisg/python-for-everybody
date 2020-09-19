file_name = input("Enter a file name: ")
count = 0
total = 0

try:
    open_file = open(file_name)

except:
    print("File cannot be opened:", file_name)
    exit()

for line in open_file.readlines():
    if line.startswith('X-DSPAM-Confidence:'):
        colon = line.find(": ")
        num = line[colon + 1:]
        number = float(num)
        count = count + 1

        total = total + number
    else:
        continue

print("Average Spam Confidence:", total/count)
