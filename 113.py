# extract from digits in string

def extract_digits(s):
    digits = ''.join(filter(str.isdigit, s))
    return digits

print(extract_digits("abc123def456"))  # Output: "123456"