# reverse orde in string 

def reverse_order(s):
    words = s.split()
    reversed_order = words[::-1]
    return ' '.join(reversed_order)
print(reverse_order("Hello World"))  # Output: "World Hello"