# count consonants in string

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)
print(count_consonants("Hello, World!"))  # Output: 7