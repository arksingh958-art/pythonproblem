# find key value maximum

my_dict = {'a': 10, 'b': 20, 'c': 5}
max_key = max(my_dict, key=my_dict.get)
max_value = my_dict[max_key]
print(f"Key with maximum value: {max_key}, Value: {max_value}")