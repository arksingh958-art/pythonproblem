# find  word frequency in string
def word_frequency(s, word):
    words = s.split()
    return words.count(word)
print(word_frequency("Hello, World! Hello everyone!", "Hello"))  # Output: 2