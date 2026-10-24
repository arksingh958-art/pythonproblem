# armstrong number function
def is_armstrong(num):
    order = len(str(num))
    return num == sum(int(digit) ** order for digit in str(num))

print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
