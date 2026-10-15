# shoping cart dictionary 
cart = {
    'item1': {'name': 'Apple', 'quantity': 3, 'price': 0.5},
    'item2': {'name': 'Banana', 'quantity': 5, 'price': 0.2},
    'item3': {'name': 'Orange', 'quantity': 2, 'price': 0.3},
    'item4': {'name': 'Grapes', 'quantity': 1, 'price': 1.0}
}

# Accessing values in the nested dictionary
print("Name of item1:", cart['item1']['name'])  # Output: Name of item1: Apple
print("Quantity of item2:", cart['item2']['quantity'])  # Output: Quantity of item2: 5
print("Price of item3:", cart['item3']['price'])  # Output: Price of item3: 0.3
print("Name of item4:", cart['item4']['name'])  # Output: Name of item4: Grapes
print("Quantity of item4:", cart['item4']['quantity'])  # Output: Quantity of item4: 1
print("Price of item4:", cart['item4']['price'])  # Output: Price of item4: 1.0