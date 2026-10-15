#  short dictoionary by values
dict1 = {'a': 10, 'b': 20, 'c': 30}
sorted_dict = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
print(f"Dictionary sorted by values: {sorted_dict}")