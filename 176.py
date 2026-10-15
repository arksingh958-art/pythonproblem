#  find missing keys in two dictionaqry 

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
missing_keys = dict1.keys() - dict2.keys()
print(missing_keys)