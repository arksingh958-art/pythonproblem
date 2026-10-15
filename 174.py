# find duplicates

dict1 = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
duplicates = {key: value for key, value in dict1.items() if list(dict1.values()).count(value) > 1}
print(duplicates)