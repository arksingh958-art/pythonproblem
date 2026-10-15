# invert key / values

dict1 = {'a': 10, 'b': 20, 'c': 30}
inverted_dict = {v: k for k, v in dict1.items()}
print(f"Inverted dictionary: {inverted_dict}")