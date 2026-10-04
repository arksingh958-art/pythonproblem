#  find shortest word in string

def shortest_word(s):
    words = s.split()
    shortest = min(words, key=len)
    return shortest

print(shortest_word("The quick brown fox jumps over the lazy dog"))  # Output: "The"