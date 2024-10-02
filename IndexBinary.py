def index_bits(binary_string):
    # Check if the input is a valid binary string
    if not set(binary_string).issubset({'0', '1'}):
        return "Invalid input. Please enter a binary string."

    # Create a list of tuples with each bit and its index
    indexed_bits = [(bit, idx + 1) for idx, bit in enumerate(binary_string)]
    return indexed_bits

# Example usage
binary_input = input("Enter a binary string: ")
result = index_bits(binary_input)

print(result)
