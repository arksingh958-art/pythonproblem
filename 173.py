# group word by first letter
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
grouped_words = {}
for word in words:
    first_letter = word[0]
    if first_letter not in grouped_words:
        grouped_words[first_letter] = []
    grouped_words[first_letter].append(word)
    
print(grouped_words)