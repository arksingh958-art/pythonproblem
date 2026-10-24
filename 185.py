 # multiple return values
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

result_sum, result_product = calculate(3, 4)
print("Sum:", result_sum)
print("Product:", result_product)