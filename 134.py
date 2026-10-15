# find second smallest no

num = (1, 2, 3, 4, 5, 1, 2, 3)

unique_numbers= list(set(num))
unique_numbers.sort()
second_smallest = unique_numbers[1] if len(unique_numbers) > 1 else None
print(second_smallest)
