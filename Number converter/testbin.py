def decimal_to_binary(decimal_str):
    # Split the decimal string into integer and fractional parts
    integer_part, fractional_part = decimal_str.split('.')

    # Convert integer part to binary
    binary_integer = bin(int(integer_part))[2:]

    # Convert fractional part to binary
    fractional_part_value = float('0.' + fractional_part)
    binary_fractional = ''

    # Calculate binary representation of fractional part
    for _ in range(8):  # Considering 8 bits for fractional part
        fractional_part_value *= 2
        bit = int(fractional_part_value)
        binary_fractional += str(bit)
        fractional_part_value -= bit

    # Print the binary representation
    print(f"{binary_integer}.{binary_fractional}")

# Get input from the user
decimal_input = input("Enter the decimal number: ")

# Call the function
decimal_to_binary(decimal_input)
