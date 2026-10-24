# Sum of digits function
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print(sum_of_digits(123))  # 6
print(sum_of_digits(456))  # 15