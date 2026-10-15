# dictionary create /update /delete /access

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing values

print(my_dict['name'])  # Output: John
# Updating values
my_dict['age'] = 31
# Adding new key-value pair
my_dict['country'] = 'USA'
# Deleting a key-value pair
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'country': 'USA'}
