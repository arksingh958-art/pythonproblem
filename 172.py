# contact book using dictionary 
contact_book = {
    'contact1': {'name': 'John Doe', 'phone': '123-456-7890', 'email': 'john.doe@email.com'},
    'contact2': {'name': 'Jane Smith', 'phone': '098-765-4321', 'email': 'jane.smith@email.com'},
    'contact3': {'name': 'Bob Johnson', 'phone': '555-123-4567', 'email': 'bob.johnson@email.com'}
}

# Accessing values in the nested dictionary
print("Name of contact1:", contact_book['contact1']['name'])  # Output: Name of contact1: John Doe
print("Phone of contact2:", contact_book['contact2']['phone'])  # Output: Phone of contact2: 098-765-4321
print("Email of contact3:", contact_book['contact3']['email'])  # Output: Email of contact3: bob.johnson@email.com