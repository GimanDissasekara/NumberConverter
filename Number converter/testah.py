f = open('HexaNumbers.txt','r')
myList = []
for line in f:
    myList.append(line.strip())
print(myList)
print(myList[1])


# Specify the file name
file_name = 'output.txt'

# Open the file in write mode
with open(file_name, 'w') as file:
    # Write each number to a new line in the file
    for number in myList:
        file.write(f"{number}\n")


# List of numbers
numbers = [1.5, 2.3, 4.7, 3.2, 5.8]

# Specify the file name
file_name = 'output.txt'

# Open the file in write mode
with open(file_name, 'w') as file:
    # Write each number to a new line in the file
    for number in numbers:
        file.write(f"{number}\n")
