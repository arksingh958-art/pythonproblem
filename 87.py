# perfect number

def is_perfect(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

print(is_perfect(6))   # Output: True
print(is_perfect(28))  # Output: True
print(is_perfect(12))  # Output: False