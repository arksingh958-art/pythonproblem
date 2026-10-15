# count character frequency using dictionary
text = "hello world"

char_frequency = {}
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)