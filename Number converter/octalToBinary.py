def octal_digit_to_binary(octal_digit):
    try:
        # Convert octal digit to binary
        binary_digit = bin(int(octal_digit))[2:].zfill(3)

        return binary_digit
    except ValueError:
        return "Invalid octal digit"

def octal_to_binary_with_split(octal_number):
    binary_result = ""

    for digit in octal_number:
        if digit == '.':
            binary_result += '.'
        else:
            binary_result += octal_digit_to_binary(digit)

    return binary_result

# # Example usage:
# octal_input = input("Enter an octal number: ")
# binary_result = octal_to_binary_with_split(octal_input)

# print(f"The binary equivalent of {octal_input} is: {binary_result}")

#open the textfile and add numbers for a list
f = open('HexaNumbers.txt','r')
myNumList = []
for line in f:
    myNumList.append(line.strip())

#Print one by one Hexa decimal numbers
for i in myNumList:
    octal_input=i
    binary_result = octal_to_binary_with_split(octal_input)
    print(binary_result)