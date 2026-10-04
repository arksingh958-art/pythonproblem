# capitalize words in string
def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

print(capitalize_words("hello world"))  # Output: "Hello World"