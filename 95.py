# count special characters in string
def count_special_characters(s):
    special_chars = "!@#$%^&*()-+"
    return sum(1 for char in s if char in special_chars)

print(count_special_characters("Hello, World! 123"))  # Output: 2