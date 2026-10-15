# rotate list by n position
numbers = [1, 2, 3, 4, 5]

n = 2  # number of positions to rotate
rotated_list = numbers[n:] + numbers[:n]
print(rotated_list)