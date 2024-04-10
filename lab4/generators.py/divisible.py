def generate_numbers_divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
n = int(input("Enter a number (n): "))

# Generate numbers divisible by 3 and 4 up to n
divisible_numbers_generator = generate_numbers_divisible_by_3_and_4(n)

# Print the numbers
print("Numbers divisible by 3 and 4:", list(divisible_numbers_generator))