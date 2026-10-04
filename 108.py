# reverse each  word in a string 

def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
print(reverse_words("Hello World"))  # Output: "olleH dlroW"