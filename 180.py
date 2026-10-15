# create frequency dictionary for a list of words
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
frequency_dict = {}
for word in words:
    frequency_dict[word] = frequency_dict.get(word, 0) + 1
print(frequency_dict)