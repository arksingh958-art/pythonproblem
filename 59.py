# triangle valid hai ya nhi 

a= float(input(" enter side 1:"))
b= float(input(" enter side 2:"))
c = float(input(" enter side 3 :"))

if  a + b> c and a + c> b and b + c > a:
    print(" valid triangle")
else:
    print (" invalid triangle")