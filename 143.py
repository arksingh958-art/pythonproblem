# finding missing number 

num=[ 1,2,3,4,6,7,8,9,10]
missing = [x for x in range(1, 11) if x not in num]
print(missing)