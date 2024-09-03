def hex_digit_to_binary(hex_digit):
    try:
        # Convert Hex digit to binary
        decimal_value = int(hex_digit, 16)
        binary_digit = bin(decimal_value)[2:].zfill(4)

        return binary_digit
    except ValueError:
        return "Invalid hexadecimal digit"

def hex_to_binary_with_split(hex_number):
    binary_result = ""

    for digit in hex_number:
        if digit == '.':
            binary_result += '.'
        else:
            binary_result += hex_digit_to_binary(digit)

    return binary_result


#open the textfile and add numbers for a list
f = open('HexadecimalNumbers.txt','r')
myNumList = []
for line in f:
    myNumList.append(line.strip())



#Print one by one Hexa decimal numbers
for i in myNumList:
     hex_input=i
     binary_result = hex_to_binary_with_split(hex_input.upper())
     print(binary_result)
