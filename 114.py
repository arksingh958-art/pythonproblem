# check string contains in alphabetical order

def is_alphabetical(s):
    return s == ''.join(sorted(s))

print(is_alphabetical("abc"))  # Output: True
print(is_alphabetical("bac"))  # Output: False