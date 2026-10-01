# find a smallest digit

num = int(input("enter a number "))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10
print("smallest digit:", smallest)