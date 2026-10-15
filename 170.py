# nested dictionary 

dict1 = {
    'student1': {'name': 'Alice', 'age': 20, 'marks': 85},
    'student2': {'name': 'Bob', 'age': 22, 'marks': 90},
    'student3': {'name': 'Charlie', 'age': 21, 'marks': 78},
    'student4': {'name': 'David', 'age': 23, 'marks': 92}
}

# Accessing values in the nested dictionary
print("Name of student1:", dict1['student1']['name'])  # Output: Name of student1: Alice
print("Marks of student2:", dict1['student2']['marks'])  # Output: Marks of student2: 90
print("Age of student3:", dict1['student3']['age'])  # Output: Age of student3: 21
print("Name of student4:", dict1['student4']['name'])  # Output: Name of student4: David