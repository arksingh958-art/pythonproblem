# find student with highest mark
dict1 = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
highest_student = max(dict1, key=dict1.get)
print(f"Student with highest mark: {highest_student}")