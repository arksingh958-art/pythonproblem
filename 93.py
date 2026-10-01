# count digit in string

def count_digits(s):
    return sum(1 for char in s if char.isdigit())

print(count_digits("Hello, World! 123"))  # Output: 3


