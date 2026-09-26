# smallest three num

a = int(input("enter a first num:"))
b = int(input(" enter a second num"))
c = int(input("enter a third number"))

if a<=b and a<=c:
    print("smallest", a)
elif b<=c and b<=c:
    print("smallest" , b)
else:
    print("smallest" , c)