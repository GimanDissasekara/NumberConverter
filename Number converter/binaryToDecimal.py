def binary_to_decimal(binary_number):
    try:
        # Split the binary number into integer and fractional parts
        integer_part, _, fractional_part = binary_number.partition('.')

        # Convert the integer part to decimal
        decimal_integer = int(integer_part, 2)

        # Convert the fractional part to decimal
        decimal_fractional = 0
        if fractional_part:
            decimal_fractional = sum(int(bit) * 2**(-i-1) for i, bit in enumerate(fractional_part))

        # Combine the integer and fractional parts
        decimal_result = decimal_integer + decimal_fractional

        return decimal_result
    except ValueError:
        return "Invalid binary input"

# Example usage:
binary_input = input("Enter a binary number: ")
decimal_result = binary_to_decimal(binary_input)

print(f"The decimal equivalent of {binary_input} is: {decimal_result}")