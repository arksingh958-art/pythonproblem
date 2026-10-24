# calculator
def calculator(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for x in args:
            result *= x
        return result
    else:
        return "Invalid operation"

print(calculator("add", 1, 2, 3, 4, 5))
print(calculator("multiply", 2, 3, 4))