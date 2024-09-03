def grouped_fractional(fractional_part):
    # Determine the length of the last group
        last_group_length = len(fractional_part) % 3

    # Add leading zeros to the last group if needed
        binary_input_padded = fractional_part + '0' * (3 - last_group_length) if last_group_length != 0 else fractional_part

        return binary_input_padded

def group_binary_and_convert_to_hex(binary_input):
    # Split binary into integer and fractional parts
    integer_part, fractional_part = binary_input.split('.')
    
    # Group integer part into groups of 3
    grouped_integer = ' '.join([integer_part[max(i - 3, 0):i] for i in range(len(integer_part), 0, -3)][::-1])

    frac = grouped_fractional(fractional_part)
    # Convert integer and fractional parts to hexadecimal
    hex_integer = oct(int(integer_part, 2))[2:]
    hex_fractional = oct(int(frac, 2))[2:]

    # Combine results
    grouped_binary_output = f"{grouped_integer} . {grouped_fractional}"
    oct_output = f"{hex_integer.upper()}.{hex_fractional.upper()}"

    return grouped_binary_output, oct_output

# Example usage:
# binary_input = "10100.101"

# Open the textfile and add numbers for a list
f = open('BinaryNumbers.txt','r')
myNumList = []
for line in f:
    myNumList.append(line.strip())

#Print one by one Hexa decimal numbers
for i in myNumList:
     binary_input=i
     grouped_binary, oct_output = group_binary_and_convert_to_hex(binary_input)
     print(oct_output)