# find lomgest word in string
def longest_word(s):
    words = s.split()
    longest = max(words, key=len)
    return longest
print(longest_word("The quick brown fox jumps over the lazy dog"))  # Output: "jumps"

