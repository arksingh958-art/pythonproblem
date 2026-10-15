# find keys that are in one dictionary but not in the other
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
unique_keys = dict1.keys() ^ dict2.keys()
print(unique_keys)