def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# Get input from the console
n = int(input("Enter a number (n): "))

# Generate even numbers up to n
even_numbers_generator = generate_even_numbers(n)

# Print the even numbers in comma-separated form
print("Even Numbers:", ", ".join(map(str, even_numbers_generator)))