def grouped_fractional(fractional_part):
    # Determine the length of the last group
        last_group_length = len(fractional_part) % 4

    # Add leading zeros to the last group if needed
        binary_input_padded = fractional_part + '0' * (4 - last_group_length) if last_group_length != 0 else fractional_part

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
f = open('BinaryNumbers.txt','r')
myNumList = []
for line in f:
    myNumList.append(line.strip())

#Print one by one Hexa decimal numbers
for i in myNumList:
     binary_input=i
     hex_output = group_binary_and_convert_to_hex(binary_input)
     print(hex_output)

