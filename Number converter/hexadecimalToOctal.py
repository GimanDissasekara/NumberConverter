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

# # print(f"The binary equivalent of {octal_input} is: {binary_result}")
# binary_input=binary_result

def grouped_fractional(fractional_part):
    # Determine the length of the last group
        last_group_length = len(fractional_part) % 3

    # Add leading zeros to the last group if needed
        binary_input_padded = fractional_part + '0' * (3 - last_group_length) if last_group_length != 0 else fractional_part

        return binary_input_padded

def group_binary_and_convert_to_hex(binary_input):
    # Split binary into integer and fractional parts
    integer_part, fractional_part = binary_input.split('.')
    
    # Group integer part into groups of 4
    grouped_integer = ' '.join([integer_part[max(i - 4, 0):i] for i in range(len(integer_part), 0, -4)][::-1])

    frac = grouped_fractional(fractional_part)
    # Convert integer and fractional parts to hexadecimal
    hex_integer = hex(int(integer_part, 2))[2:]
    hex_fractional = hex(int(frac, 2))[2:]

    # Combine results
    grouped_binary_output = f"{grouped_integer} . {grouped_fractional}"
    hex_output = f"{hex_integer.upper()}.{hex_fractional.upper()}"

    return hex_output

# Example usage:
# binary_input = "10100.101"

#open the textfile and add numbers for a list
f = open('output.txt','r')
myNumList = []
for line in f:
    myNumList.append(line.strip())
count = len(myNumList)

# open new list for save binary values
binaryList = []

#Save one by one Octal numbers in a list
for i in myNumList:
    octal_input=i
    binary_result = octal_to_binary_with_split(octal_input)
    binaryList.append(binary_result)

#Print one by one Hexa decimal numbers
for i in binaryList:
     binary_input=i
     hex_output = group_binary_and_convert_to_hex(binary_input)
     print(hex_output)
