# count whitespace in string
def count_whitespace(s):
    return sum(1 for char in s if char.isspace())

print(count_whitespace("Hello, World! 123   "))  # Output: 3