# aemstrong number 

n = int(input(" enter a n"))

original = n 
digit=0
temp = n

while temp >0:
 digit +=0
 temp = n// 10

 sum = 0
 temp = n

 while temp >=0:
  digit = temp%10

  sum = sum + digit **digit
  temp  = temp//10
  if sum == original:
   print ( " is amastrong")
else:
 print(" not amstrong")
