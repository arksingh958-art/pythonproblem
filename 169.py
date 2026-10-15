# employee salary dictionary
dict1 = {'John': 50000, 'Alice': 60000, 'Bob': 55000, 'Charlie': 70000}
# find employee with highest salary
highest_employee = max(dict1, key=dict1.get)
print(f"Employee with highest salary: {highest_employee}")