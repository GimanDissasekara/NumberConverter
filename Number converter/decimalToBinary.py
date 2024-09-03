def decimal_to_binary(decimal_str):
    # Split the decimal string into integer and fractional parts
    integer_part, fractional_part = decimal_str.split('.')

    # Convert integer part to binary
    binary_integer = bin(int(integer_part))[2:]

    # Convert fractional part to binary
    fractional_part_value =float ('0.' + fractional_part)
    binary_fractional = ''

    # Calculate binary representation of fractional part
    for x in range(8):  # Considering 8 bits for fractional part
        fractional_part_value *= 2
        bit = int(fractional_part_value)
        binary_fractional += str(bit)
        fractional_part_value -= bit

    # Print the binary representation
    deciOut=f"{binary_integer}.{binary_fractional}"
    return deciOut

#-------------------------------------------------------------------------
# Open the textfile and add numbers for a list
f = open('DecimalNumbers.txt','r')
myNumList = []
for line in f:
    myNumList.append(line.strip())

#Print one by one Hexa decimal numbers
for i in myNumList:
     decimal_input=i
     hex_output = decimal_to_binary(decimal_input)
     print(hex_output)


