# find student with lowest mark
dict1 = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
lowest_student = min(dict1, key=dict1.get)
print(f"Student with lowest mark: {lowest_student}")