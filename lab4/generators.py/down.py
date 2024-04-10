def generate_numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage:
n = int(input("Enter a number (n): "))

# Generate numbers down to 0
numbers_generator = generate_numbers_down_to_zero(n)

# Print the numbers
print("Numbers down to 0:", list(numbers_generator))