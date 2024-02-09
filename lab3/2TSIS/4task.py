def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
numbers_list = input("Enter a list of numbers separated by spaces: ").split()
numbers_list = [int(num) for num in numbers_list]

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)