# find second largest no

numbers = [1, 2, 3, 4, 5, 1, 2, 3]

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
second_largest = unique_numbers[1] if len(unique_numbers) > 1 else None
print(second_largest)
