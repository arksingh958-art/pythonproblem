# simple calulator if-elif
a= float(input ("enter  a number "))
op= input("enter a operator( + , - ,* ,/):")
b = float(input("enter  a number "))

if op== "+" :
    print("result" , "a + b")
elif op == "-":
    print("result" , "a-b")
elif op=="*":
    print("result" , "a*b")
elif op == "/":
    print("result" ,"a/b")
else:
    print("invalid opreator")