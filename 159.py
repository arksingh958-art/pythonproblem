# count word frequency
text = "hello world hello"
words = text.split()
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print(word_frequency)