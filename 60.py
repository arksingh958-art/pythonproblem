# triangle identify karo

a = float(input (" enter a side 1:"))
b = float(input(" enter a side 2 :"))
c = float(input(" enter a side 3 :"))


if a + b <= b and b + c <= a and a + c <= b:
    print (" invalid  triangle ")
elif a==b==c:
    print(" eqiletral triangle")
elif a==b and b==c and a==c:
    print(" isoscalace triangle")
else: 
    print(" scalane triangle")