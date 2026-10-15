# dictionary comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3}
# create a new dictionary with values doubled
dict2 = {key: value * 2 for key, value in dict1.items()}
print(dict2)