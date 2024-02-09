from itertools import permutations

def print_permutations(input_string):
    
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    
    print("All permutations of the string:")
    for permuted_string in permuted_strings:
        print(permuted_string)

# Example usage:
user_input = input("Enter a string: ")
print_permutations(user_input)