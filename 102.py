# # remove duplicate words from string

def remove_duplicate_words(s):
    words = s.split()
    unique_words = list(set(words))
    return ' '.join(unique_words)

print(remove_duplicate_words("Hello, World! Hello everyone!"))  # Output: "Hello, World! everyone!"